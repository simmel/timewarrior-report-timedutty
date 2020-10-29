# pylint: disable=missing-module-docstring,missing-function-docstring
from timewarrior_report_timedutty import __version__, duration


def test_version():
    assert __version__ == '0.1.0'

def test_duration_1h_30m():
    assert "P1H30M" == duration(seconds=5400)

def test_duration_2h_31m():
    assert "P2H31M" == duration(seconds=9060)
