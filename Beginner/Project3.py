even=[]
odd=[]

for i in range(1,50):
    if i%2==0:
        even.append(i)
    else: 
        odd.append(i)

print("Even numbers:", even)
print("Odd numbers:" ,odd)
