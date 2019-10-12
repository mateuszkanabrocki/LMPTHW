import os
import sys

import pytest

this_module = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(this_module, "../project/"))

from ex14 import *


def test_push():
    colors = DoubleLinkedList()
    colors._invariants()
    colors.push("Pthalo Blue")
    assert colors.count() == 1
    colors.push("Ultramarine Blue")
    assert colors.count() == 2
    colors._invariants()


def test_pop():
    colors = DoubleLinkedList()
    colors._invariants()
    colors.push("Magenta")
    colors.push("Alizarin")
    assert colors.pop() == "Alizarin"
    assert colors.pop() == "Magenta"
    assert colors.pop() is None
    colors._invariants()


def test_unshift():
    colors = DoubleLinkedList()
    colors._invariants()
    colors.push("Viridian")
    colors.push("Sap Green")
    colors.push("Van Dyke")
    assert colors.unshift() == "Viridian"
    assert colors.unshift() == "Sap Green"
    assert colors.unshift() == "Van Dyke"
    assert colors.unshift() is None
    colors._invariants()


def test_shift():
    colors = DoubleLinkedList()
    colors._invariants()
    colors.shift("Cadmium Orange")
    assert colors.count() == 1

    colors.shift("Carbazole Violet")
    assert colors.count() == 2
    assert colors.pop() == "Carbazole Violet"
    assert colors.count() == 1
    assert colors.pop() == "Cadmium Orange"
    assert colors.count() == 0
    colors._invariants()


def test_remove():
    colors = DoubleLinkedList()
    colors._invariants()
    colors.push("Cobalt")
    colors.push("Zinc White")
    colors.push("Nickle Yellow")
    colors.push("Perinone")
    assert colors.remove("Cobalt") == 0
    colors.dump("before perinone")
    assert colors.remove("Perinone") == 2
    colors.dump("after perinone")
    assert colors.remove("Nickle Yellow") == 1
    colors.dump("after perinone")
    assert colors.remove("Zinc White") == 0
    colors._invariants()


def test_first():
    colors = DoubleLinkedList()
    colors._invariants()
    colors.push("Cadmium Red Light")
    assert colors.first() == "Cadmium Red Light"
    colors.push("Hansa Yellow")
    assert colors.first() == "Cadmium Red Light"
    colors.shift("Pthalo Green")
    assert colors.first() == "Cadmium Red Light"
    colors._invariants()


def test_last():
    colors = DoubleLinkedList()
    colors._invariants()
    colors.push("Cadmium Red Light")
    assert colors.last() == "Cadmium Red Light"
    colors.push("Hansa Yellow")
    assert colors.last() == "Hansa Yellow"
    colors.shift("Pthalo Green")
    assert colors.last() == "Pthalo Green"
    colors._invariants()


def test_get():
    colors = DoubleLinkedList()
    colors.push("Vermillion")
    assert colors.get(0) == "Vermillion"
    colors.push("Sap Green")
    assert colors.get(0) == "Vermillion"
    assert colors.get(1) == "Sap Green"
    colors.push("Cadmium Yellow Light")
    assert colors.get(0) == "Vermillion"
    assert colors.get(1) == "Sap Green"
    assert colors.get(2) == "Cadmium Yellow Light"
    assert colors.pop() == "Cadmium Yellow Light"
    assert colors.get(0) == "Vermillion"
    assert colors.get(1) == "Sap Green"
    assert colors.get(2) is None
    colors.pop()
    assert colors.get(0) == "Vermillion"
    colors.pop()
    assert colors.get(0) is None
