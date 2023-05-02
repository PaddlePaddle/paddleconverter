
import sys
import os
sys.path.append(os.path.dirname(__file__) + '/../')

import textwrap
from tests.apibase import APIBase

class RandLikeAPI(APIBase):

    def __init__(self, pytorch_api) -> None:
        super().__init__(pytorch_api)

    def check(self, pytorch_result, paddle_result):
        if pytorch_result.requires_grad == paddle_result.stop_gradient:
            return False
        if str(pytorch_result.dtype)[6:] != str(paddle_result.dtype)[7:]:
            return False
        if pytorch_result.requires_grad:
            torch_numpy, paddle_numpy = pytorch_result.detach().numpy(), paddle_result.numpy()
        else:
            torch_numpy, paddle_numpy = pytorch_result.numpy(), paddle_result.numpy()
        if torch_numpy.shape != paddle_numpy.shape:
            return False
        return True

obj = RandLikeAPI('torch.rand_like')

def test_case_1():
    pytorch_code = textwrap.dedent(
        '''
        import torch
        a = torch.zeros(3, 4, dtype=torch.float64)
        result = torch.rand_like(a)
        '''
    )
    obj.run(pytorch_code, ['result'])

def test_case_2():
    pytorch_code = textwrap.dedent(
        '''
        import torch
        a = torch.zeros(3, 4, dtype=torch.float64)
        result = torch.rand_like(a, dtype=torch.float32, requires_grad=True)
        '''
    )
    obj.run(pytorch_code, ['result'])

def test_case_3():
    pytorch_code = textwrap.dedent(
        '''
        import torch
        a = torch.zeros(3, 4, dtype=torch.float64)
        flag = True
        result = torch.rand_like(a, dtype=torch.float32, requires_grad=flag)
        '''
    )
    obj.run(pytorch_code, ['result'])

def test_case_4():
    pytorch_code = textwrap.dedent(
        '''
        import torch
        result = torch.rand_like(torch.zeros(3, 4, dtype=torch.float64), dtype=torch.float32, requires_grad=True)
        '''
    )
    obj.run(pytorch_code, ['result'])

def test_case_5():
    pytorch_code = textwrap.dedent(
        '''
        import torch
        result = torch.rand_like(input=torch.zeros(3, 4, dtype=torch.float64), dtype=torch.float32, requires_grad=True)
        '''
    )
    obj.run(pytorch_code, ['result'])