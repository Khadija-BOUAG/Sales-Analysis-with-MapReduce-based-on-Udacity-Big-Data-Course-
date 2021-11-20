#!/usr/bin/env python3

import sys
# total sales and the total nb of sales for each store

current_store = None
sumSales = 0
nbSales = 0

for line in sys.stdin :
    try :
        store, sales, count = line.strip().split('\t')
        sales = float(sales)
        count = int(count)
    except :
        continue

    if current_store == store :
        sumSales += sales
        nbSales += count
    else :
        if current_store :
            print(current_store, '\t', sumSales, '\t', nbSales)
        current_store = store
        sumSales = sales
        nbSales = count

if current_store :
    print(current_store, '\t', sumSales, '\t', nbSales)