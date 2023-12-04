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

import textwrap

from apibase import APIBase

obj = APIBase("torch.asin")


def test_case_1():
    pytorch_code = textwrap.dedent(
        """
        import torch
        result = torch.asin(torch.tensor([0.34, -0.56, 0.73]))
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_2():
    pytorch_code = textwrap.dedent(
        """
        import torch
        a = torch.tensor([0.34, -0.56, 0.73])
        result = torch.asin(a)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_3():
    pytorch_code = textwrap.dedent(
        """
        import torch
        a = [0.34, -0.56, 0.73]
        out = torch.tensor(a)
        result = torch.asin(torch.tensor(a), out=out)
        """
    )
    obj.run(pytorch_code, ["out", "result"])


def test_case_4():
    pytorch_code = textwrap.dedent(
        """
        import torch
        a = [0.34, -0.56, 0.73]
        out = torch.tensor(a)
        result = torch.asin(input=torch.tensor(a), out=out)
        """
    )
    obj.run(pytorch_code, ["out", "result"])


def test_case_5():
    pytorch_code = textwrap.dedent(
        """
        import torch
        a = [0.34, -0.56, 0.73]
        out = torch.tensor(a)
        result = torch.asin(out=out, input=torch.tensor(a))
        """
    )
    obj.run(pytorch_code, ["out", "result"])
