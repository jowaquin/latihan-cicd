import re

import pytest

import kalkulator


def test_tambah():
    assert kalkulator.tambah(2, 3) == 5


def test_kurang():
    assert kalkulator.kurang(5, 3) == 2


def test_kali():
    assert kalkulator.kali(4, 3) == 12


def test_bagi():
    assert kalkulator.bagi(10, 2) == 5


def test_bagi_nol():
    with pytest.raises(ValueError):
        kalkulator.bagi(1, 0)


def test_format_versi_semver():
    assert re.fullmatch(r"\d+\.\d+\.\d+", kalkulator.__version__)
