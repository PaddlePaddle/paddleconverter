# Copyright (c) 2024 PaddlePaddle Authors. All Rights Reserved.
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

obj = APIBase("torchvision.models.mobilenet_v3_large")


def test_case_1():
    pytorch_code = textwrap.dedent(
        """
        import torchvision
        mobilenet_v3_large = torchvision.models.mobilenet_v3_large()
        """
    )
    paddle_code = textwrap.dedent(
        """
        import paddle
        mobilenet_v3_large = paddle.vision.models.mobilenet_v3_large(pretrained=False)
        """
    )
    obj.run(
        pytorch_code,
        expect_paddle_code=paddle_code,
    )


def test_case_2():
    pytorch_code = textwrap.dedent(
        """
        import torchvision
        mobilenet_v3_large = torchvision.models.mobilenet_v3_large(weights=None, progress=False)
        """
    )
    paddle_code = textwrap.dedent(
        """
        import paddle
        mobilenet_v3_large = paddle.vision.models.mobilenet_v3_large(progress=False,
            pretrained=False)
        """
    )
    obj.run(
        pytorch_code,
        expect_paddle_code=paddle_code,
    )


def test_case_3():
    pytorch_code = textwrap.dedent(
        """
        import torchvision
        mobilenet_v3_large = torchvision.models.mobilenet_v3_large(progress=True, weights='DEFAULT')
        """
    )
    paddle_code = textwrap.dedent(
        """
        import paddle
        mobilenet_v3_large = paddle.vision.models.mobilenet_v3_large(progress=True,
            pretrained=True)
        """
    )
    obj.run(
        pytorch_code,
        expect_paddle_code=paddle_code,
    )


def test_case_4():
    pytorch_code = textwrap.dedent(
        """
        import torchvision
        mobilenet_v3_large = torchvision.models.mobilenet_v3_large(weights=torchvision.models.MobileNet_V3_Large_Weights.DEFAULT)
        """
    )
    paddle_code = textwrap.dedent(
        """
        import paddle
        mobilenet_v3_large = paddle.vision.models.mobilenet_v3_large(pretrained=True)
        """
    )
    obj.run(
        pytorch_code,
        expect_paddle_code=paddle_code,
    )


def test_case_5():
    pytorch_code = textwrap.dedent(
        """
        import torchvision
        mobilenet_v3_large = torchvision.models.mobilenet_v3_large(progress=True)
        """
    )
    paddle_code = textwrap.dedent(
        """
        import paddle
        mobilenet_v3_large = paddle.vision.models.mobilenet_v3_large(progress=True,
            pretrained=False)
        """
    )
    obj.run(
        pytorch_code,
        expect_paddle_code=paddle_code,
    )
