from src.app import print_name
import pytest

def test_ester_gottlieb():
    assert print_name() == "Ester Gottlieb!"
