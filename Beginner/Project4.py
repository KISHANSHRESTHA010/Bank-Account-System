Fizz_Buzz=[]
Fizz=[]
Buzz=[]
normal=[]

for i in range(1,101):
    if i%3==0 and i%5==0:
        Fizz_Buzz.append(i)
    elif i%3==0 and i%5!=0:
        Fizz.append(i)
    elif i%5==0 and i%3!=0:
        Buzz.append(i)
    else:
        normal.append(i)

print("FrizzBuzz numbers:", Fizz_Buzz)
print("Frizznumbers:", Fizz)
print("Buzz numbers:",Buzz)
print("Normal:",normal)

