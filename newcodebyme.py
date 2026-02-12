a=float(input('Price of book 1:'))
b=float(input('price of book 2:'))
c=float(input('price of book 3:'))
print('Price of book 1:%.2f'%a)
print('Price of book 2:%.2f'%b)
print('Price of book 3:%.2f'%c)
t=(a+b+c)
print('Total Amount:%.2f'%t)
if(t>500):
    e=(t*0.10)
print('Discount:%.2f'%e)
f=t-e
print('Final Amount:%.2f'%f)
