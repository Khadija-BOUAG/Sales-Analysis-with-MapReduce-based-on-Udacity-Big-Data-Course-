#!/usr/bin/env python3

import sys
# max individual sales for each store

current_store = 0
max_sales = 0

for line in sys.stdin :
    try :
        store, sales = line.split('\t')
        sales = int(float(sales))
    except :
        continue

    if current_store == store :
        if max_sales < sales :
            max_sales = sales

    else :
        if current_store :
            print(current_store, '\t', max_sales)
        current_store = store
        max_sales = sales

if current_store :
    print(store, '\t', max_sales)

