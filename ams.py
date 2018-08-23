
lower = 100
upper = 2000
for num1 in range(lower, upper + 1):
   order = len(str(num1))
   sum1 = 0
   temp1 = num1
   while temp1 > 0:
       digit = temp1 % 10
       sum1 += digit ** order
       temp1 //= 10

   if num1 == sum1:
       print(num1)
