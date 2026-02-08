temp=int(input(""))
if temp<0:
    print("Freezing weather")
elif(0>temp<10):
    print("Very Cold weather")
elif(10>temp<20):
    print("Cold weather")
elif(20>temp<30):
    print("Normal in temp")
elif(30>temp<40):
    print("its hot")
else:
    print("very hot")
