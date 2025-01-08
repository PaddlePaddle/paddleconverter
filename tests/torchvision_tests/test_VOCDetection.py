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

obj = APIBase("torchvision.datasets.VOCDetection")


def test_case_1():
    pytorch_code = textwrap.dedent(
        """
        import torchvision
        root_path = './data'
        train_dataset = torchvision.datasets.VOCDetection(root=root_path, image_set='trainval')
        """
    )
    paddle_code = textwrap.dedent(
        """
        import os

        import paddle

        ############################## 相关utils函数，如下 ##############################


        def VOCDetection(*args, **kwargs):
            root = kwargs.pop("root")
            year = kwargs.pop("year", "2012")
            if year != "2012":
                raise ValueError("PaddlePaddle only supports VOC2012 dataset")
            image_set = kwargs.pop("image_set", "train")
            download = kwargs.pop("download", True)
            transform = kwargs.pop("transform", None)

            if image_set == "trainval":
                mode = "train"
            elif image_set == "train":
                mode = "test"
            elif image_set == "val":
                mode = "valid"
            else:
                raise ValueError("Only supports image_set in ['trainval', 'train', 'val']")

            data_file = os.path.join(root, "VOCtrainval_11-May-2012.tar")
            return paddle.vision.datasets.VOC2012(data_file=data_file, mode=mode, transform=transform, download=download, backend=None)

        ############################## 相关utils函数，如上 ##############################


        root_path = "./data"
        train_dataset = VOCDetection(root=root_path, image_set="trainval")
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
        root_path = './data'
        train_dataset = torchvision.datasets.VOCDetection(root=root_path, image_set='train')
        """
    )
    paddle_code = textwrap.dedent(
        """
        import os

        import paddle

        ############################## 相关utils函数，如下 ##############################


        def VOCDetection(*args, **kwargs):
            root = kwargs.pop("root")
            year = kwargs.pop("year", "2012")
            if year != "2012":
                raise ValueError("PaddlePaddle only supports VOC2012 dataset")
            image_set = kwargs.pop("image_set", "train")
            download = kwargs.pop("download", True)
            transform = kwargs.pop("transform", None)

            if image_set == "trainval":
                mode = "train"
            elif image_set == "train":
                mode = "test"
            elif image_set == "val":
                mode = "valid"
            else:
                raise ValueError("Only supports image_set in ['trainval', 'train', 'val']")

            data_file = os.path.join(root, "VOCtrainval_11-May-2012.tar")
            return paddle.vision.datasets.VOC2012(data_file=data_file, mode=mode, transform=transform, download=download, backend=None)

        ############################## 相关utils函数，如上 ##############################


        root_path = "./data"
        train_dataset = VOCDetection(root=root_path, image_set="train")
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
        root_path = './data'
        train_dataset = torchvision.datasets.VOCDetection(root_path)
        """
    )
    paddle_code = textwrap.dedent(
        """
        import os

        import paddle

        ############################## 相关utils函数，如下 ##############################


        def VOCDetection(*args, **kwargs):
            root = kwargs.pop("root")
            year = kwargs.pop("year", "2012")
            if year != "2012":
                raise ValueError("PaddlePaddle only supports VOC2012 dataset")
            image_set = kwargs.pop("image_set", "train")
            download = kwargs.pop("download", True)
            transform = kwargs.pop("transform", None)

            if image_set == "trainval":
                mode = "train"
            elif image_set == "train":
                mode = "test"
            elif image_set == "val":
                mode = "valid"
            else:
                raise ValueError("Only supports image_set in ['trainval', 'train', 'val']")

            data_file = os.path.join(root, "VOCtrainval_11-May-2012.tar")
            return paddle.vision.datasets.VOC2012(data_file=data_file, mode=mode, transform=transform, download=download, backend=None)

        ############################## 相关utils函数，如上 ##############################


        root_path = "./data"
        train_dataset = VOCDetection(root=root_path)
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
        root_path = './data'
        train_dataset = torchvision.datasets.VOCDetection(image_set='trainval', download=False, root=root_path)
        """
    )
    paddle_code = textwrap.dedent(
        """
        import os

        import paddle

        ############################## 相关utils函数，如下 ##############################


        def VOCDetection(*args, **kwargs):
            root = kwargs.pop("root")
            year = kwargs.pop("year", "2012")
            if year != "2012":
                raise ValueError("PaddlePaddle only supports VOC2012 dataset")
            image_set = kwargs.pop("image_set", "train")
            download = kwargs.pop("download", True)
            transform = kwargs.pop("transform", None)

            if image_set == "trainval":
                mode = "train"
            elif image_set == "train":
                mode = "test"
            elif image_set == "val":
                mode = "valid"
            else:
                raise ValueError("Only supports image_set in ['trainval', 'train', 'val']")

            data_file = os.path.join(root, "VOCtrainval_11-May-2012.tar")
            return paddle.vision.datasets.VOC2012(data_file=data_file, mode=mode, transform=transform, download=download, backend=None)

        ############################## 相关utils函数，如上 ##############################


        root_path = "./data"
        train_dataset = VOCDetection(image_set="trainval", download=False, root=root_path)
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
        root_path = './data'
        train_dataset = torchvision.datasets.VOCDetection(root=root_path, image_set='trainval', transform=None, download=False)
        """
    )
    paddle_code = textwrap.dedent(
        """
        import os

        import paddle

        ############################## 相关utils函数，如下 ##############################


        def VOCDetection(*args, **kwargs):
            root = kwargs.pop("root")
            year = kwargs.pop("year", "2012")
            if year != "2012":
                raise ValueError("PaddlePaddle only supports VOC2012 dataset")
            image_set = kwargs.pop("image_set", "train")
            download = kwargs.pop("download", True)
            transform = kwargs.pop("transform", None)

            if image_set == "trainval":
                mode = "train"
            elif image_set == "train":
                mode = "test"
            elif image_set == "val":
                mode = "valid"
            else:
                raise ValueError("Only supports image_set in ['trainval', 'train', 'val']")

            data_file = os.path.join(root, "VOCtrainval_11-May-2012.tar")
            return paddle.vision.datasets.VOC2012(data_file=data_file, mode=mode, transform=transform, download=download, backend=None)

        ############################## 相关utils函数，如上 ##############################


        root_path = "./data"
        train_dataset = VOCDetection(
            root=root_path, image_set="trainval", transform=None, download=False
        )
        """
    )
    obj.run(
        pytorch_code,
        expect_paddle_code=paddle_code,
    )
