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

obj = APIBase("torch.cuda.amp.GradScaler")


def _test_case_1():
    pytorch_code = textwrap.dedent(
        """
        import torch
        scaler = torch.cuda.amp.GradScaler()
        x = torch.tensor([[[-1.3020, -0.1005,  0.5766,  0.6351, -0.8893,  0.0253, -0.1756, 1.2913],
                            [-0.8833, -0.1369, -0.0168, -0.5409, -0.1511, -0.1240, -1.1870, -1.8816]]])
        with torch.cuda.amp.autocast():
            loss = torch.mean(x*x).to('cuda')
        scaled = scaler.scale(loss).cpu()  # scale the loss
        result = scaled
        """
    )
    obj.run(pytorch_code, ["result"])


def _test_case_2():
    pytorch_code = textwrap.dedent(
        """
        import torch
        scaler = torch.cuda.amp.GradScaler(init_scale=32768,growth_interval=1000)
        x = torch.tensor([[[-1.3020, -0.1005,  0.5766,  0.6351, -0.8893,  0.0253, -0.1756, 1.2913],
                            [-0.8833, -0.1369, -0.0168, -0.5409, -0.1511, -0.1240, -1.1870, -1.8816]]])
        with torch.cuda.amp.autocast():
            loss = torch.mean(x*x).to('cuda')
        scaled = scaler.scale(loss).cpu()  # scale the loss
        result = scaled

        """
    )
    obj.run(pytorch_code, ["result"])
