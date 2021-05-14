# TODO(everyone): 더하기, 빼기, 곱하기, 나누기 함수 테스트 케이스 작성
# test code from https://github.com/l-yohai/devops-eng-training/blob/main/unittest/functions_test.py
import pytest
import os
import sys
sys.path.append(
    os.path.dirname(os.path.dirname(__file__))
)
from functions import add, sub, div, mul


def test_add():
    assert add(1,3) == 4 
    assert add('1', '2') == str(1 + 2)
    assert add(1, '2') == "Query Parameter's Data Type is not a String."
    assert add('1', 2) == "Query Parameter's Data Type is not a String."
    assert add('a', '2') == "Num1 is not a Number."
    assert add('2', 'b') == "Num2 is not a Number."
    assert add('a', 'b') == "Num1 is not a Number."


def test_sub():
    assert sub(6, 4) == 2
    assert sub(4, 6) == -2
    assert sub('5', '3') == str(5 - 3)
    assert sub(1, '2') == "Query Parameter's Data Type is not a String."
    assert sub('1', 2) == "Query Parameter's Data Type is not a String."
    assert sub('a', '2') == "Num1 is not a Number."
    assert sub('2', 'b') == "Num2 is not a Number."
    assert sub('a', 'b') == "Num1 is not a Number."

def test_mul():
    assert mul(1.5, 4) == 6
    assert mul('4', '6') == str(4 * 6)
    assert mul(1, '2') == "Query Parameter's Data Type is not a String."
    assert mul('1', 2) == "Query Parameter's Data Type is not a String."
    assert mul('a', '2') == "Num1 is not a Number."
    assert mul('2', 'b') == "Num2 is not a Number."
    assert mul('a', 'b') == "Num1 is not a Number."

def test_div():
    assert div(5,3) == "5/3"
    assert div('8', '2') == str(8 / 2)
    assert div(1, '2') == "Query Parameter's Data Type is not a String."
    assert div('1', 2) == "Query Parameter's Data Type is not a String."
    assert div('a', '2') == "Num1 is not a Number."
    assert div('2', 'b') == "Num2 is not a Number."
    assert div('a', 'b') == "Num1 is not a Number."
    assert div('2', '0') == 'division by zero'




