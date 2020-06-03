# pcost.py
#
# Exercise 1.27

totalPrice = 0.00

with open('Data/portfolio.csv','rt') as f:
    headers = next(f)
    for line in f:
        arraySplit = line.split(',')
        price = float(arraySplit[2])*float(arraySplit[1])
        totalPrice += price

print(totalPrice)

""" alternatively 
can jsut use the open alone, but need to close at the end

f =open(file)

do things witth f..

f.close()

 """


