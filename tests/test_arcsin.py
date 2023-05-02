
import sys
import os
sys.path.append(os.path.dirname(__file__) + '/../')

import textwrap
from tests.apibase import APIBase


obj = APIBase('torch.arcsin')

def test_case_1():
    pytorch_code = textwrap.dedent(
        '''
        import torch
        result = torch.arcsin(torch.tensor([0.34, -0.56, 0.73]))
        '''
    )
    obj.run(pytorch_code,['result'])

def test_case_2():
    pytorch_code = textwrap.dedent(
        '''
        import torch
        a = torch.tensor([0.34, -0.56, 0.73])
        result = torch.arcsin(a)
        '''
    )
    obj.run(pytorch_code, ['result'])

def test_case_3():
    pytorch_code = textwrap.dedent(
        '''
        import torch
        a = [0.34, -0.56, 0.73]
        out = torch.tensor(a)
        result = torch.arcsin(torch.tensor(a), out=out)
        '''
    )
    obj.run(pytorch_code, ['out', 'result'])
