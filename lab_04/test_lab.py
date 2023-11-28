import pytest
import main
import csv
from io import StringIO
import os

def test_01():
    
    in_str = '5 * (3 + 7) / (4 - 2) ^ 2'
    rpn = main.get_rpn(in_str)
    ans = main.calc_rpn(rpn)
    assert ans == [2.5]

def test_02():
    
    in_str = '( 100 / 50 - 1 ) / 10'
    rpn = main.get_rpn(in_str)
    ans = main.calc_rpn(rpn)
    assert ans == [0.1]

def test_03():
    
    in_str = '12 / 4 + ( 8 / 2 ) ^ 2'
    rpn = main.get_rpn(in_str)
    ans = main.calc_rpn(rpn)
    assert ans == [18]  
    
def test_04():
    
    in_str = '9 * (6 - 2) / (5 + 5) ^ 2'
    rpn = main.get_rpn(in_str)
    ans = main.calc_rpn(rpn)
    assert ans == [0.09]

def test_05():
    
    in_str = '( 20 / 10 - 2 ) * 3'
    rpn = main.get_rpn(in_str)
    ans = main.calc_rpn(rpn)
    assert ans == [-3.0]  

