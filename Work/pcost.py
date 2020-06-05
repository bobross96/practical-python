# pcost.py
#
# Exercise 1.27
import csv

totalPrice = 0.00

""" with open('Data/portfolio.csv','rt') as f:
    headers = next(f)
    for line in f:
        arraySplit = line.split(',')
        price = float(arraySplit[2])*float(arraySplit[1])
        totalPrice += price

print(totalPrice) """

with open('Data/portfolio.csv') as f:
    test = csv.reader(f)
    next(test)
    rows = next(test)
    #print(rows)
    
    """ t = (rows[0],int(rows[1]), float(rows[2]))
    #print(t)
    cost = t[1]*t[2]
    print(f'{cost:0.2f}') """
    d = {
        'name' : rows[0],
        'shares' : int(rows[1]),
        'price'  : float(rows[2])
    }    
    cost = d['price'] * d['shares']
    d['date'] = (5,6,2020)
    d['date'][0] = 3




""" alternatively 
can jsut use the open alone, but need to close at the end

f =open(file)

do things witth f..

f.close()

 """


