# pylint: disable=missing-module-docstring,missing-function-docstring
from timewarrior_report_timedutty import __time_intervals, __version__


def gurken(*, seconds):
    return "P1H30M"

def test_version():
    assert __version__ == '0.1.0'

def test_duration_1h_30m():
    assert "P1H30M" == gurken(seconds=5400)

def test_duration_2h_31m():
    assert "P2H31M" == gurken(seconds=9060)
