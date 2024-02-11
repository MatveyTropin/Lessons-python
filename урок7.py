"""number=int(input("Type your number?"))
if number %2==0:
    print("yuor number is even!")
else:
    print("your number is odd!")
"""
temp=int(input("your temperature outside?"))
if temp <0:
    print("Wear warm clothes!")
elif temp>=0 and temp<10:
    print("It is cold,but not forget warm clothes!")
elif temp>=10 and temp<20:
    print("It is normal, go for walk!")
elif temp>=20 and temp <30:
    print("It is hot!Buy an icecream!")
else:
    print("It is very hot!Need some water")