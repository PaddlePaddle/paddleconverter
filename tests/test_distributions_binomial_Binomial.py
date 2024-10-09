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

obj = APIBase("torch.distributions.binomial.Binomial")


def test_case_1():
    pytorch_code = textwrap.dedent(
        """
        import torch
        m = torch.distributions.binomial.Binomial(total_count=100, probs=torch.tensor([0, .2, .8, 1]), validate_args=False)
        result = m.sample()
        """
    )
    obj.run(
        pytorch_code,
        ["result"],
        check_value=False,
    )


def test_case_2():
    pytorch_code = textwrap.dedent(
        """
        import torch
        m = torch.distributions.binomial.Binomial(1, probs=None, logits=torch.tensor([0.3]))
        result = m.sample()
        """
    )
    obj.run(
        pytorch_code,
        ["result"],
        unsupport=True,
        reason="paddle does not support this parameter logits",
    )


def test_case_3():
    pytorch_code = textwrap.dedent(
        """
        import torch
        m = torch.distributions.binomial.Binomial(5, torch.tensor([0.3]), validate_args=False)
        result = m.sample()
        """
    )
    obj.run(
        pytorch_code,
        ["result"],
        check_value=False,
    )


def test_case_4():
    pytorch_code = textwrap.dedent(
        """
        import torch
        m = torch.distributions.binomial.Binomial(1, torch.tensor([0.3]), validate_args=False)
        result = m.sample()
        """
    )
    obj.run(
        pytorch_code,
        ["result"],
        check_value=False,
    )


def test_case_5():
    pytorch_code = textwrap.dedent(
        """
        import torch
        m = torch.distributions.binomial.Binomial(probs=torch.tensor([0, .2, .8, 1]), total_count=100, validate_args=False)
        result = m.sample()
        """
    )
    obj.run(
        pytorch_code,
        ["result"],
        check_value=False,
    )


def test_case_6():
    pytorch_code = textwrap.dedent(
        """
        import torch
        m = torch.distributions.binomial.Binomial(probs=torch.tensor([0, .2, .8, 1]))
        result = m.sample()
        """
    )
    obj.run(
        pytorch_code,
        ["result"],
        check_value=False,
    )


def test_case_7():
    pytorch_code = textwrap.dedent(
        """
        import torch
        m = torch.distributions.binomial.Binomial(logits=torch.tensor(0.2))
        result = m.sample()
        """
    )
    obj.run(
        pytorch_code,
        ["result"],
        unsupport=True,
        reason="paddle does not support this parameter logits",
    )
