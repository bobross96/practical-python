# mortgage.py
#
# Exercise 1.7

monthsPaid = 0
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
extra_payment = 1000
extra_payment_start_month = 60
extra_payment_end_month = 108


while principal > 0:
    if (monthsPaid >= extra_payment_start_month and monthsPaid <= extra_payment_end_month):
        principal = principal * (1+rate/12) - payment - extra_payment
        total_paid = total_paid + payment + extra_payment
        monthsPaid+= 1
    else:
        #print('normal one')
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment
        monthsPaid+= 1
    print(monthsPaid,total_paid,principal)
    if principal < 0:
        total_paid = total_paid + principal
        principal = 0
print(monthsPaid,'Total paid', total_paid,principal)