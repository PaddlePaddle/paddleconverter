# Copyright (c) 2023 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import argparse
import json
import os
import re
import sys

import pytest

sys.path.append(os.path.dirname(__file__) + "/../../tests")

import apibase

output_dir = os.path.dirname(__file__)

whitelist_pattern = [
    r"^test_(\w*)Tensor\.py",
    r"^test_distributed_all_gather_object\.py",
    r"^test_hub_download_url_to_file\.py",
    r"^test_Size\.py",
]


def get_test_cases(discovery_paths=["tests"]):
    # Collect the test cases
    monkeypatch = pytest.MonkeyPatch()
    unittest_data = {}
    pytest.main(
        discovery_paths + [], plugins=[RecordAPIRunPlugin(monkeypatch, unittest_data)]
    )
    return unittest_data


class RecordAPIRunPlugin:
    def __init__(self, monkeypatch, data):
        self.monkeypatch = monkeypatch
        self.collected_items = data
        self.whitelist_re = [re.compile(p) for p in whitelist_pattern]
        originapi = apibase.APIBase.run

        def update_record(api, code):
            records = self.collected_items.get(api, [])
            records.append(code)
            self.collected_items.update({api: records})

        def record_and_run(self, *args, **kwargs):
            pytorch_api = self.pytorch_api
            assert len(args) > 0
            pytorch_code = args[0]
            update_record(pytorch_api, pytorch_code)
            return originapi(self, *args, **kwargs)

        monkeypatch.setattr(apibase.APIBase, "run", record_and_run)

    def __del__(self):
        self.monkeypatch.undo()

    def pytest_collection_modifyitems(self, items):
        # Mount the monkeypatch
        collected = []
        for item in items:
            for w_pat in self.whitelist_re:
                if w_pat.match(item.nodeid):
                    break
            else:
                collected.append(item)

        items[:] = collected


def extract_api_name(api, code: str):
    api_seg = api.split(".")
    for i in range(len(api_seg)):
        api_nickname = ".".join(api_seg[i:])
        if code.find(api_nickname) >= 0:
            return api_nickname
    else:
        raise ValueError(f"{api} not found in {repr(code)}")


def extract_params_from_invoking(api, code: str):
    args, kwargs = [], []
    api_name = extract_api_name(api, code)
    idx = code.find(api_name)
    assert idx >= 0, f"api_name {api_name} must exists."

    code, idx = code[idx + len(api_name) :], 0

    pair_stack = []
    key = None

    # 寻找参数列表的结束位置
    for i, c in enumerate(code):
        if c == "(" or c == "[":
            pair_stack.append(c)
            if len(pair_stack) == 1 and c == "(":
                idx = i + 1
        elif c == "=":
            if len(pair_stack) == 1:
                key = code[idx:i]
                idx = i + 1
        elif c == "," or c == ")" or c == "]":
            if len(pair_stack) == 1:
                value = code[idx:i]
                if len(value.strip()) > 0:
                    if key is not None:
                        assert (
                            key not in kwargs
                        ), f"duplicated key {key} in {repr(code)}"
                        kwargs.append((key, value))
                        key = None
                    else:
                        args.append(value)
                idx = i + 1
            if c == ")":
                assert pair_stack[-1] == "(", f"Unpaired in {repr(code)}"
                pair_stack.pop()
                if len(pair_stack) == 0:
                    break
            elif c == "]":
                assert pair_stack[-1] == "[", f"Unpaired in {repr(code)}"
                pair_stack.pop()

    if len(pair_stack) != 0:
        raise ValueError(f"Unpaired in {repr(code)}")

    return args, kwargs


def match_subsequence(pattern, obj):
    """
    验证 obj 是 pattern 的子序列
    """
    i, j = 0, 0

    while i < len(pattern) and j < len(obj):
        if pattern[i] == obj[j]:
            j += 1
        i += 1

    return j == len(obj)


def check_call_variety(test_data, api_mapping):
    report = {}
    for api, code_list in test_data.items():
        if api not in api_mapping:
            print(f"api {api} not found in api_mapping")
            continue

        mapping_data = api_mapping[api]

        if "min_input_args" not in mapping_data:
            print(f"{api} has no mapping data 'min_input_args'.")
            continue
        min_input_args = mapping_data["min_input_args"]

        if "args_list" not in mapping_data and min_input_args != 0:
            print(f"{api} has no mapping data 'args_list'.")
            continue

        args_list = mapping_data.get("args_list", [])
        args_list_without_key = (
            args_list.copy()
            if "*" not in args_list
            else args_list[: args_list.index("*")]
        )
        args_list_with_key = args_list.copy()
        if "*" in args_list_with_key:
            args_list_with_key.remove("*")

        all_args = False
        all_kwargs = False
        not_subsequence = False

        for code in code_list:
            try:
                api_name = extract_api_name(api, code)
                args, kwargs = extract_params_from_invoking(api, code)
            except Exception as e:
                print(f'Error when extract params from invoking "{api}"')
                print(e)
                exit(-1)

            if len(args) + len(kwargs) < min_input_args:
                raise ValueError(
                    f"{api}(*{args}, **{kwargs}) not meet min_input_args={min_input_args}"
                )

            if len(args) == len(args_list_without_key):
                all_args = True

            keys = [k[0].strip() for k in kwargs]
            if len(keys) == len(args_list_with_key) and match_subsequence(
                args_list_with_key, keys
            ):
                all_kwargs = True
            if len(args_list_with_key) <= 1 or not match_subsequence(
                args_list_with_key, keys
            ):
                not_subsequence = True

            # if api == 'torch.Tensor.add':
            #     print(args_list_with_key, keys)
            #     print(all_args, all_kwargs, not_subsequence, code)

        if all_args and all_kwargs and not_subsequence:
            continue

        report[api] = {
            "all args": all_args,
            "all kwargs": all_kwargs,
            "kwargs out of order": not_subsequence,
        }

        if not all_args:
            print(f"{api} has no unittest with all arguments without keyword.")
        if not all_kwargs:
            print(f"{api} has no unittest with all arguments with keyword.")
        if not not_subsequence and len(args_list) > 1:
            print(f"{api} has no unittest with keyword arguments out of order.")

    return report


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Call Variety Check v0.1")
    parser.add_argument(
        "path", type=str, nargs="+", help="Path to test directory or file"
    )
    parser.add_argument(
        "--rerun", "-r", action="store_true", default=False, help="Rerun tests"
    )
    parser.add_argument(
        "--no-check", action="store_true", default=False, help="Disable check"
    )
    parser.add_argument(
        "--report", action="store_true", default=True, help="Generate report"
    )

    args = parser.parse_args()

    with open("paconvert/api_mapping.json", "r") as f:
        api_mapping = json.load(f)
    with open("paconvert/api_alias_mapping.json", "r") as f:
        api_alias_mapping = json.load(f)

    test_data_path = os.path.join(output_dir, "unittest_data.json")

    if os.path.exists(test_data_path) and os.path.isfile(test_data_path):
        with open(test_data_path, "r") as f:
            test_data = json.load(f)
    else:
        args.rerun = True
        test_data = {}

    if args.rerun:
        newtest_data = get_test_cases(args.path)
        test_data.update(newtest_data)
        with open(test_data_path, "w") as f:
            json.dump(test_data, f)

    for k, v in api_alias_mapping.items():
        if v in api_mapping:
            api_mapping[k] = api_mapping[v]
        elif k in api_mapping:
            api_mapping[v] = api_mapping[k]
        else:
            if k not in test_data and v not in test_data:
                pass
            if k not in api_mapping and v not in api_mapping:
                if k in test_data:
                    test_data.pop(k)
                    print(f"skip {k} from test_data because of no mapping.")
                if v in test_data:
                    test_data.pop(v)
                    print(f"skip {v} from test_data because of no mapping.")
            else:
                ka, va = k in api_mapping, v in api_mapping
                kd, vd = k in test_data, v in test_data
                raise ValueError(
                    f"({k}, {v}) not found in api_mapping, {ka} {va}, {kd} {vd}."
                )

    if not args.no_check:
        report = check_call_variety(test_data, api_mapping)

        if args.report:
            report_outpath = os.path.join(output_dir, "callvariety_report.md")
            with open(report_outpath, "w") as f:
                f.write("# Call Variety Report\n\n")

                columns = ["api", "all args", "all kwargs", "kwargs out of order"]
                f.write(f'| {" | ".join(columns)} |\n')
                f.write(f'| {" | ".join(["---"] * len(columns))} |\n')
                for api, data in report.items():
                    item2desc = lambda v: "✅" if v else "❌"
                    f.write(
                        f'| {api} | {" | ".join([item2desc(data[k]) for k in columns[1:]])} |\n'
                    )
