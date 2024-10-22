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

obj = APIBase("torch.linalg.slogdet")


def test_case_1():
    pytorch_code = textwrap.dedent(
        """
        import torch
        a = torch.tensor([[[ 0.9254, -0.6213],
            [-0.5787,  1.6843]],

            [[ 0.3242, -0.9665],
            [ 0.4539, -0.0887]],

            [[ 1.1336, -0.4025],
            [-0.7089,  0.9032]]])
        result = torch.linalg.slogdet(a)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_2():
    pytorch_code = textwrap.dedent(
        """
        import torch
        a = torch.tensor([[[ 0.9254, -0.6213],
            [-0.5787,  1.6843]],

            [[ 0.3242, -0.9665],
            [ 0.4539, -0.0887]],

            [[ 1.1336, -0.4025],
            [-0.7089,  0.9032]]])
        result = torch.linalg.slogdet(a)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_3():
    pytorch_code = textwrap.dedent(
        """
        import torch
        x = torch.tensor([[ 0.7308,  1.0060,  0.5270,  1.4516],
                        [-0.1383,  1.5706,  0.4724,  0.4141],
                        [ 0.1193,  0.2829,  0.9037,  0.3957],
                        [-0.8202, -0.6474, -0.1631, -0.6543]])
        out = (torch.tensor(0.), torch.tensor(0.))
        result = torch.linalg.slogdet(A=x, out=out)
        """
    )
    obj.run(pytorch_code, ["result", "out"])


# generated by validate_unittest autofix, based on test_case_3
def test_case_4():
    pytorch_code = textwrap.dedent(
        """
        import torch
        x = torch.tensor([[ 0.7308,  1.0060,  0.5270,  1.4516],
                        [-0.1383,  1.5706,  0.4724,  0.4141],
                        [ 0.1193,  0.2829,  0.9037,  0.3957],
                        [-0.8202, -0.6474, -0.1631, -0.6543]])
        out = (torch.tensor(0.), torch.tensor(0.))
        result = torch.linalg.slogdet(out=out, A=x)
        """
    )
    obj.run(pytorch_code, ["result", "out"])


def test_case_5():
    pytorch_code = textwrap.dedent(
        """
        import torch
        x = torch.tensor([[-3.0832+3.0494j, -0.1751+0.1449j,  1.2197+1.8188j,  4.0353-0.7416j],
                        [-2.9842-2.8928j,  0.2123+0.6190j, -2.6104+0.7303j,  1.9740+3.3802j],
                        [ 0.4939-2.4271j,  0.5006-0.6895j, -1.3655-0.2352j, -1.6636+1.6514j],
                        [-4.1212+0.1513j,  0.7119-0.0603j, -1.7803+2.8278j,  3.4966+1.2988j]])
        result1, result2 = torch.linalg.slogdet(x)
        """
    )
    obj.run(pytorch_code, ["result1", "result2"])
