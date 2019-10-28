#! /usr/bin/env python
import pytest
from time import strftime,localtime

def func(x):
    return x+1

def test_one():
    assert func(5) == 5

@pytest.mark.parametrize('test_input,expected',[(1,0)])
def test_two(test_input,expected):
    assert test_input == expected 

if __name__=='__main__':
    file_name = strftime('%y%m%d%H%M%S',localtime())
    pytest.main(['demo.py','-q','--html={}.html'.format(file_name)])
