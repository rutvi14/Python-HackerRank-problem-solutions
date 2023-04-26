#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


if __name__ == "__main__":
    s = input()
    s = sorted(s)
    freq = Counter(list(s))

    count = Counter(s)
    for k, v in freq.most_common(3):
        print(k, v)
