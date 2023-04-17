
import re
import sys
import os
sys.path.append(os.path.dirname(__file__) + '/../')

import textwrap

from tests.apibase import APIBase


class LongTensorAPI(APIBase):

    def __init__(self, pytorch_api) -> None:
        super().__init__(pytorch_api)

    def check(self, pytorch_result, paddle_result):
        if pytorch_result.requires_grad == paddle_result.stop_gradient:
            return False
        if str(pytorch_result.dtype)[6:] != str(paddle_result.dtype)[7:]:
            return False
        return True

obj = LongTensorAPI('torch.LongTensor')

def test_case_1():
    pytorch_code = textwrap.dedent(
        '''
        import torch
        result = torch.LongTensor(2, 3)
        '''
    )
    obj.run(pytorch_code, ['result'])

def test_case_2():
    pytorch_code = textwrap.dedent(
        '''
        import torch
        shape = [2, 3]
        result = torch.LongTensor(*shape)
        '''
    )
    obj.run(pytorch_code, ['result'])

def test_case_3():
    pytorch_code = textwrap.dedent(
        '''
        import torch
        dim1, dim2 = 2, 3
        result = torch.LongTensor(dim1, dim2)
        '''
    )
    obj.run(pytorch_code, ['result'])

def test_case_4():
    pytorch_code = textwrap.dedent(
        '''
        import torch
        def fun(x: torch.LongTensor):
            return x * 2

        a = torch.LongTensor(3, 4)
        result = fun(a)
        '''
    )
    obj.run(pytorch_code, ['result'])

def test_case_5():
    pytorch_code = textwrap.dedent(
        '''
        import torch
        result = torch.LongTensor([[3, 4], [5, 8]])
        '''
    )
    obj.run(pytorch_code, ['result'])

def test_case_6():
    pytorch_code = textwrap.dedent(
        '''
        import torch
        a = torch.tensor([[3, 4], [5, 8]])
        result = torch.LongTensor(a)
        '''
    )
    obj.run(pytorch_code, ['result'])

def test_case_7():
    pytorch_code = textwrap.dedent(
        '''
        import torch
        result = torch.LongTensor((1, 2, 3))
        '''
    )
    obj.run(pytorch_code, ['result'])

def _test_case_8():
    pytorch_code = textwrap.dedent(
        '''
        import torch
        result = torch.LongTensor()
        '''
    )
    obj.run(pytorch_code, ['result'])