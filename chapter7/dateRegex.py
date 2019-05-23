#! /usr/bin/python3
# dateRegex.py -  Replaces dates in different formats with dates in dd/mm/yyyy format.

import re

dateRegex = re.compile(r'''(
    (3[01]|[12][0-9]|0?[1-9])
    (/|-|.)
    (0?[1-9]|1[0-2])
    (/|-|.)
    ([0-9]{4})
    )''', re.VERBOSE)

text = 'I was born on 6.03.2003\n \
    Today is 21/5/2019 \
    and tomorrow will 22-05-2019'

