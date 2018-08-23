lowers = 900
uppers = 1000
print("Prime numbers between",lowers,"and",uppers,"are:")

for num1 in range(lowers,uppers + 1):
   # prime numbers are greater than 1
   if num1 > 1:
       for i in range(2,num1):
           if (num1 % i) == 0:
               break
       else:
           print(num1)
