import os
import sys

import pytest

this_module = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(this_module, "../project/"))

from stack import *


def test_push():
    """Pushes a new value to the top of the stack."""
    colors = Stack()
    colors._invariants()
    assert colors.count() == 0
    colors.push('red')
    assert colors.top() == 'red'
    assert colors.count() == 1
    colors.push('blue')
    colors.dump("***test_push***")
    assert colors.top() == 'blue'
    assert colors.count() == 2

def test_pop():
    """Pops the value that is currently on the top of the stack."""
    colors = Stack()
    colors.push('red')
    colors.push('blue')
    colors.pop()
    colors._invariants()
    assert colors.top() == 'red'
    assert colors.count() == 1
    colors.pop()
    assert colors.top() == None
    assert colors.count() == 0

def test_top():
    """Returns a *reference* to the first/top item, does not remove."""
    colors = Stack()
    assert colors.top() == None
    colors.push('red')
    assert colors.top() == 'red'
    colors.push('blue')
    assert colors.top() == 'blue'

def test_count():
    """Counts the number of elements in the stack."""
    colors = Stack()
    assert colors.top() == None
    assert colors.count() == 0
    colors.push('red')
    assert colors.top() == 'red'
    assert colors.count() == 1
    colors.push('blue')
    assert colors.top() == 'blue'
    assert colors.count() == 2
    colors._invariants()
    colors.pop()
    assert colors.top() == 'red'
    colors.dump("***test_count1***")
    assert colors.count() == 1
    colors.pop()
    assert colors.top() == None
    assert colors.count() == 0
    colors.dump("***test_count1***")
    colors.push('red')
    assert colors.top() == 'red'
    assert colors.count() == 1
