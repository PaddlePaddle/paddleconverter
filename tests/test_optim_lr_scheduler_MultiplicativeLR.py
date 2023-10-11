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

obj = APIBase("torch.optim.lr_scheduler.MultiplicativeLR")


def generate_torch_code(scheduler_init: str):
    return """
    import torch
    inp = torch.tensor([[[[ 0.65819663, -1.44500113,  0.03488150, -0.11252647,  0.64591473,
              -0.25023264,  1.43210626, -0.17528275, -0.41327286, -1.42921889],
              [ 1.01807046, -0.15144072,  0.25586420,  0.66442668, -0.74051994,
                0.27811581,  0.19295734, -1.85243905, -0.21655996, -1.31090474],
              [ 1.11078060,  0.76435864, -0.58546644, -1.60248399,  1.21102262,
                1.84995520, -0.59313560, -0.43019459, -1.22067058,  1.12034869],
              [-0.59133518,  0.57231778, -2.04297185, -2.65964627,  1.86213946,
                0.69934291, -0.43929303,  0.79671234,  0.73919666, -0.23766366],
              [ 1.33526826,  0.77814531,  0.72026747,  0.01414320, -1.82173848,
              -0.10328550, -0.66961199,  1.68644571, -0.27223003, -0.70142502],
              [ 0.30492339, -1.49054408, -0.55506420,  0.68340236,  0.19797169,
              -1.07023966,  1.82865989, -0.87176341,  0.18112634,  0.47510919],
              [ 0.42837384,  1.01021397,  0.30776358,  0.07036194,  1.59942043,
              -0.41225538, -0.30321866,  0.84667981, -1.53250265, -0.03019625],
              [ 0.54298091, -0.14060315, -1.13251436,  0.37944487, -0.42639804,
              -1.04459620, -1.15721095,  0.02442988,  1.25040483, -0.14369141],
              [ 0.48817471, -0.22014830, -0.39481393, -1.18876767,  0.27675587,
                0.11846039, -0.55626374,  0.04168135,  0.24947685, -0.89958537],
              [-0.85359418, -0.36227068, -1.17553079, -0.15267773, -0.03734926,
                1.00306797, -1.35028768, -0.35130620,  0.76797879, -0.66623610]]]])
    conv = torch.nn.Conv2d(1, 1, 3)
    weight = torch.tensor([[[[ 0.7787, -0.5682, -0.1042],
              [ 0.7353, -0.2635,  0.7900],
              [-0.3153,  0.0752, -0.2045]]]])
    bias = torch.tensor([0.0])
    conv.weight = torch.nn.Parameter(weight)
    conv.bias = torch.nn.Parameter(bias)

    sgd = torch.optim.SGD(conv.parameters(), lr=0.1)
    scheduler = {}
    for epoch in range(1, 11):
        out = conv(inp)
        loss = torch.mean(out)
        loss.backward()
        sgd.step()
        scheduler.step()
    result1 = conv.weight
    result2 = conv.bias
  """.format(
        scheduler_init
    )


def test_case_1():
    pytorch_code = textwrap.dedent(
        generate_torch_code(
            "torch.optim.lr_scheduler.MultiplicativeLR(sgd, lambda x:0.95**x)"
        )
    )
    obj.run(pytorch_code, ["result1", "result2"], rtol=1.0e-5)


def test_case_2():
    pytorch_code = textwrap.dedent(
        generate_torch_code(
            "torch.optim.lr_scheduler.MultiplicativeLR(sgd, lr_lambda=lambda x:0.95**x)"
        )
    )
    obj.run(pytorch_code, ["result1", "result2"], rtol=1.0e-5)


def test_case_3():
    pytorch_code = textwrap.dedent(
        generate_torch_code(
            "torch.optim.lr_scheduler.MultiplicativeLR(optimizer=sgd, lr_lambda=lambda x:0.95**x)"
        )
    )
    obj.run(pytorch_code, ["result1", "result2"], rtol=1.0e-5)


def test_case_4():
    pytorch_code = textwrap.dedent(
        generate_torch_code(
            "torch.optim.lr_scheduler.MultiplicativeLR(optimizer=sgd, lr_lambda=lambda x:0.95**x, last_epoch=-1, verbose=True)"
        )
    )
    obj.run(pytorch_code, ["result1", "result2"], rtol=1.0e-5)


def test_case_5():
    pytorch_code = textwrap.dedent(
        generate_torch_code(
            "torch.optim.lr_scheduler.MultiplicativeLR(optimizer=sgd, lr_lambda=lambda x:0.95**x, verbose=True)"
        )
    )
    obj.run(pytorch_code, ["result1", "result2"], rtol=1.0e-5)


def test_case_6():
    pytorch_code = textwrap.dedent(
        generate_torch_code(
            "torch.optim.lr_scheduler.MultiplicativeLR(sgd, lambda x:0.95**x, -1, False)"
        )
    )
    obj.run(pytorch_code, ["result1", "result2"], rtol=1.0e-5)
