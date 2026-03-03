k,a,b,c,d=map(float,input().split())
const1=a*k
const2=b*k
const3=c*k
total=const1+const2+const3+(d*k)
print(f"cost for gadget1:{const1:.2f}")
print(f"cost for gadget2:{const2:.2f}")
print(f"cost for gadget3:{const3:.2f}")
print(f"Total Rental Cost:{total:.2f}")
