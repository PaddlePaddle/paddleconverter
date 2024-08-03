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

obj = APIBase("torch.cuda.Stream")


def test_case_1():
    pytorch_code = textwrap.dedent(
        """
        import torch
        if torch.cuda.is_available():
            stream = torch.cuda.Stream()
            result = stream.query()
        else:
            result = 1
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_2():
    pytorch_code = textwrap.dedent(
        """
        import torch
        if torch.cuda.is_available():
            stream = torch.cuda.Stream(priority=0)
            result = stream.query()
        else:
            result = 1
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_3():
    pytorch_code = textwrap.dedent(
        """
        import torch
        if torch.cuda.is_available():
            stream = torch.cuda.Stream(priority=-1)
            result = stream.query()
        else:
            result = 1
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_4():
    pytorch_code = textwrap.dedent(
        """
        import torch
        if torch.cuda.is_available():
            stream = torch.cuda.Stream(device=1)
            result = stream.query()
        else:
            result = 1
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_5():
    pytorch_code = textwrap.dedent(
        """
        import torch
        if torch.cuda.is_available():
            stream = torch.cuda.Stream(device=1,priority=-1)
            result = stream.query()
        else:
            result = 1
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_6():
    pytorch_code = textwrap.dedent(
        """
        import torch
        if torch.cuda.is_available():
            stream = torch.cuda.Stream(device='cuda:1',priority=-1)
            result = stream.query()
        else:
            result = 1
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_7():
    pytorch_code = textwrap.dedent(
        """
        import torch
        if torch.cuda.is_available():
            stream = torch.cuda.Stream(device='cuda',priority=-1)
            result = stream.query()
        else:
            result = 1
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_8():
    pytorch_code = textwrap.dedent(
        """
        import torch
        if torch.cuda.is_available():
            num = 1
            stream = torch.cuda.Stream(device=num,priority=-1)
            result = stream.query()
        else:
            result = 1
        """
    )
    obj.run(pytorch_code, ["result"])
