bill_thickness = 0.11 * 0.001
sears_height = 442 
num_bills = 1 
day = 1

while num_bills*bill_thickness < sears_height:
    #print(day,num_bills,num_bills*bill_thickness)
    day = day + 1
    num_bills = num_bills*2

#print('final height is ' , str(num_bills*bill_thickness) , "asdasdasdds")


d = False
if not d:
    print('its true')
else:
    print('its false')

