list=[1,2,4,2,6,7,1,2,3,8,7,8,9,7]

final=[]

for i in list:
    if i not in final:
        final.append(i)

print(final)