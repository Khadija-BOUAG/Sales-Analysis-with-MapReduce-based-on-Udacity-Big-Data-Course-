#!/usr/bin/env python3

import sys
# max individual sales for each store
for line in sys.stdin :
    try :
        date, time, store, category, sales, wayPur = line.strip().split('\t')
        print(store,"\t", sales)
    except :
        continue