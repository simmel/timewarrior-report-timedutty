# pylint: disable=missing-module-docstring,missing-function-docstring
__version__ = '0.1.0'

import logging
import sys
from collections import OrderedDict
from typing import Dict

import timewreport.parser

# weeks? = 5 days a week 144000
# days = 8 hours in a day 28800
# hours = 3600
# minutes = 60
__time_intervals = OrderedDict({
    "H": 3600,
    "M": 60,
    })

logger = logging.getLogger('timedutty')

def main() -> None:
    parser = timewreport.parser.TimeWarriorParser(sys.stdin)

    totals: Dict[str, timewreport.interval.TimeWarriorInterval] = dict()

    for interval in parser.get_intervals():
        tracked = interval.get_duration()

        tag = " ".join(interval.get_tags())
        if tag in totals:
            totals[tag] += tracked
        else:
            totals[tag] = tracked

    # Determine largest tag width.
    max_width = len('Total')

    for tag in totals:
        if len(tag) > max_width:
            max_width = len(tag)

    # Compose report header.
    print('Total by Tag')
    print('')

    # Compose table header.
    print('{:{width}} {:>10}'.format('Tag', 'Total', width=max_width))
    print('{} {}'.format('-' * max_width, '----------'))

    # Compose table rows.
    grand_total = 0
    for tag in sorted(totals):
        formatted = duration(seconds=totals[tag].total_seconds())
        grand_total += totals[tag].total_seconds()
        print('{:{width}} {:10}'.format(tag, formatted, width=max_width))

    # Compose total.
    print('{} {}'.format(' ' * max_width, '----------'))
    print('{:{width}} {:10}'.format('Total', duration(seconds=grand_total), width=max_width))

def duration(*, seconds: int) -> str:
    duration = "P" # pylint: disable=redefined-outer-name
    for interval, interval_seconds in __time_intervals.items():
        logger.debug("%s is %s long", interval, interval_seconds)
        (interval_value, seconds) = divmod(seconds, interval_seconds)
        duration += str(int(interval_value))
        duration += interval
        logger.debug("%s is %s and left %s", interval, interval_value, seconds)
    return duration
