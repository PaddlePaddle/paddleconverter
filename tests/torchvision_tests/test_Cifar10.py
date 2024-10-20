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

obj = APIBase("torchvision.datasets.CIFAR10")


def test_case_1():
    pytorch_code = textwrap.dedent(
        """
        import torchvision
        root_path = './data'
        train_dataset = torchvision.datasets.CIFAR10(root=root_path, train=True)
        """
    )
    paddle_code = textwrap.dedent(
        """
        from pathlib import Path
        import paddle
        root_path = './data'
        train_dataset = paddle.vision.datasets.Cifar10(data_file=str(Path(root_path
            ) / 'cifar-10-python.tar.gz'), mode='train')
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
        train = True
        train_dataset = torchvision.datasets.CIFAR10(root='./data', train=train)
        """
    )
    paddle_code = textwrap.dedent(
        """
        from pathlib import Path
        import paddle
        train = True
        train_dataset = paddle.vision.datasets.Cifar10(data_file=str(Path('./data') /
            'cifar-10-python.tar.gz'), mode='train' if train else 'test')
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
        train_dataset = torchvision.datasets.CIFAR10(train=True, download=True)
        """
    )
    paddle_code = textwrap.dedent(
        """
        from pathlib import Path
        import paddle
        train_dataset = paddle.vision.datasets.Cifar10(download=True, mode='train')
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
        train_dataset = torchvision.datasets.CIFAR10(root='./data', train=True)
        """
    )
    paddle_code = textwrap.dedent(
        """
        from pathlib import Path
        import paddle
        train_dataset = paddle.vision.datasets.Cifar10(data_file=str(Path('./data') /
            'cifar-10-python.tar.gz'), mode='train')
        """
    )
    obj.run(
        pytorch_code,
        expect_paddle_code=paddle_code,
    )
