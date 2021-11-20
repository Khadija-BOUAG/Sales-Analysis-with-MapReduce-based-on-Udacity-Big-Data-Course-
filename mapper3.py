#!/usr/bin/env python3

import sys
# total sales and the total nb of sales for each store
for line in sys.stdin :
    try :
        date, time, store, category, sales, wayPur = line.strip().split('\t')
        print(store,"\t", sales, '\t', 1)
    except :
        continue