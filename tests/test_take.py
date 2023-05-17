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

import os
import sys

sys.path.append(os.path.dirname(__file__) + "/../")

import textwrap

from tests.apibase import APIBase

obj = APIBase("torch.take")


def test_case_1():
    pytorch_code = textwrap.dedent(
        """
        import torch
        input = torch.tensor([[4, 3, 5],
                              [6, 7, 8]])
        result = torch.take(input, torch.tensor([0, 2, 5]))
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_2():
    pytorch_code = textwrap.dedent(
        """
        import torch
        result = torch.take(torch.empty(2, 3), index = torch.tensor([0, 3, 5]))
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_3():
    pytorch_code = textwrap.dedent(
        """
        import torch
        index = torch.tensor([3, 5, 5])
        result = torch.take(torch.tensor([[4, 3, 5],
                              [6, 7, 8]]), index)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_4():
    pytorch_code = textwrap.dedent(
        """
        import torch
        index = torch.tensor([3, 5, 5])
        x = torch.tensor([[4, 3, 5],
                          [6, 7, 8],
                          [10, 14, 13]])
        result = torch.take(input = x, index = index)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_5():
    pytorch_code = textwrap.dedent(
        """
        import torch
        result = torch.take(torch.tensor([[1, 4, 5], [7, 8, 9]]), torch.tensor([3, 5, 4]))
        """
    )
    obj.run(pytorch_code, ["result"])
