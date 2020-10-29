# pylint: disable=missing-module-docstring,missing-function-docstring
__version__ = '0.1.0'

import math
import sys

from timewreport.parser import TimeWarriorParser


def main():
    parser = TimeWarriorParser(sys.stdin)

    totals = dict()

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
        formatted = math.ceil(totals[tag].seconds / 60 / 60)
        grand_total += math.ceil(totals[tag].seconds / 60 / 60)
        print('{:{width}} {:10}'.format(tag, formatted, width=max_width))

    # Compose total.
    print('{} {}'.format(' ' * max_width, '----------'))
    print('{:{width}} {:10}'.format('Total', grand_total, width=max_width))
