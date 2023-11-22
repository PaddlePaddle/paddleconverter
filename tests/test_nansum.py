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

import textwrap

from apibase import APIBase

obj = APIBase("torch.nansum")


def test_case_1():
    pytorch_code = textwrap.dedent(
        """
        import torch
        input = torch.tensor([[1, 2], [3., float("nan")]])
        result = torch.nansum(input)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_2():
    pytorch_code = textwrap.dedent(
        """
        import torch
        input = torch.tensor([[1, 2], [3., float("nan")]])
        result = torch.nansum(input, 0)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_3():
    pytorch_code = textwrap.dedent(
        """
        import torch
        input = torch.tensor([[1, 2], [3., float("nan")]])
        result = torch.nansum(input=input, dim=1, keepdim=True)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_4():
    pytorch_code = textwrap.dedent(
        """
        import torch
        input = torch.tensor([[1, 2], [3., float("nan")]])
        result = torch.nansum(input, 1, True, dtype=torch.float64)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_5():
    pytorch_code = textwrap.dedent(
        """
        import torch
        input = torch.tensor([[1, 2], [3., float("nan")]])
        out = torch.tensor([[1, 2], [3., float("nan")]], dtype=torch.float64)
        dim, keepdim = 1, False
        result = torch.nansum(input, dim, keepdim, dtype=torch.float64, out=out)
        """
    )
    obj.run(pytorch_code, ["result"])
