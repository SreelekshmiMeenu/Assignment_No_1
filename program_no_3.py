L1=int(input("Enter the length of the first side: "))
L2=int(input("Enter the length of the second side: "))
L3=int(input("Enter the length of the third side: "))
L4=int(input ("Enter the length of the fourth side: "))
if((L1==L3) and (L1!=L4)) and ((L2==L4) and (L2!=L3)): print("Rectangle")
elif(L1==L2==L3==L4):print("Square")
else:print("not identified")

