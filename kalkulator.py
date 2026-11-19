"""Kalkulator sederhana untuk latihan CI/CD di GitHub."""

__version__ = "1.0.0"


def tambah(a, b):
    return a + b


def kurang(a, b):
    return a - b


def kali(a, b):
    return a * b


def bagi(a, b):
    if b == 0:
        raise ValueError("Pembagi tidak boleh nol")
    return a / b


if __name__ == "__main__":
    print(f"Kalkulator v{__version__}")
    print("2 + 3 =", tambah(2, 3))
