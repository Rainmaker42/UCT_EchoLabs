import pytest
import CWOTest


def test_greet():
    assert CWOTest.greet("James") == "Hello, James."


def test_sum_up():
    assert CWOTest.sum_up(502) == 7


def test_first_last():
    assert CWOTest.first_last("This is my life") == ("Ts is my le")


def test_binary_words():
    assert CWOTest.binary_words("how many times did you reboot?") == '101111'
    assert (CWOTest.binary_words("The sales guy made me bring down the website")
            == "111001011")
