#!/usr/bin/env python3

import sys
# nb of sales product categories
current_category = None
nb_sales = 0

for line in sys.stdin :
    try :
        category, sales = line.split('\t')
        sales = int(sales)
    except :
        continue

    if current_category == category:
        nb_sales += sales

    else:
        if current_category:
            print('%s\t%s' % (current_category, nb_sales))
        current_category = category
        nb_sales = sales

if current_category==category:
    print('%s\t%s' % (current_category, nb_sales))





