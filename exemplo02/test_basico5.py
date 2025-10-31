from funcoes import *


def test_email_valido():
    assert email_valido("iago.schuller@faf") is True
    assert email_valido("tralarei.222") is False

def test_dividir():
    assert dividir(3,2) == 1.5
    assert dividir(4,0) is None