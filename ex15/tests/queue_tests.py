import os
import sys

import pytest

this_module = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(this_module, "../project/"))

from queue2 import *


def test_shift():
    colors = Queue()
    colors._invariants()
    colors.shift("Cadmium Orange")
    assert colors.count() == 1
    colors.shift("Carbazole Violet")
    assert colors.count() == 2

def test_unshift():
    colors = Queue()
    colors._invariants()
    colors.shift("Viridian")
    colors.shift("Sap Green")
    colors.shift("Van Dyke")
    assert colors.unshift() == "Viridian"
    assert colors.unshift() == "Sap Green"
    assert colors.unshift() == "Van Dyke"
    assert colors.unshift() is None
    colors._invariants()

def test_remove():
    colors = Queue()
    colors._invariants()
    colors.shift("Cobalt")
    colors.shift("Zinc White")
    colors.shift("Nickle Yellow")
    colors.shift("Perinone")
    assert colors.remove("Cobalt") == 0
    colors.dump("before perinone")
    assert colors.remove("Perinone") == 2
    colors.dump("after perinone")
    assert colors.remove("Nickle Yellow") == 1
    colors.dump("after perinone")
    assert colors.remove("Zinc White") == 0
    colors._invariants()


def test_first():
    colors = Queue()
    colors._invariants()
    colors.shift("Cadmium Red Light")
    assert colors.first() == "Cadmium Red Light"
    colors.shift("Hansa Yellow")
    assert colors.first() == "Cadmium Red Light"


def test_last():
    colors = Queue()
    colors._invariants()
    colors.shift("Cadmium Red Light")
    assert colors.last() == "Cadmium Red Light"
    colors.shift("Hansa Yellow")
    assert colors.last() == "Hansa Yellow"


def test_get():
    colors = Queue()
    colors.shift("Vermillion")
    assert colors.get(0) == "Vermillion"
    colors.shift("Sap Green")
    assert colors.get(0) == "Vermillion"
    assert colors.get(1) == "Sap Green"
    colors.shift("Cadmium Yellow Light")
    assert colors.get(0) == "Vermillion"
    assert colors.get(1) == "Sap Green"
    assert colors.get(2) == "Cadmium Yellow Light"
