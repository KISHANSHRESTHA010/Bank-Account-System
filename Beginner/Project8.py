sentence=str(input("Enter your name: ")).lower()
vowelset=['a','e','i','o','u']
vowels=0

for j in sentence:
    if j in vowelset:
        vowels+=1

print(vowels)