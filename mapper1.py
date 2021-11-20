#!/usr/bin/env python3

import sys
# nb of sales per store per product categories
for line in sys.stdin :
    date, time, store, category, sales, wayPur = line.strip().split('\t')
    print(category, '\t', sales)