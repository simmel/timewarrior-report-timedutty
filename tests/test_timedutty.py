# pylint: disable=missing-module-docstring,missing-function-docstring
from timewarrior_report_timedutty import __time_intervals, __version__


def gurken():
    return "P1H30M"

def test_version():
    assert __version__ == '0.1.0'

def test_duration_1h_30m():
    assert "P1H30M" == gurken()
