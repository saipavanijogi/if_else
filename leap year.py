#a year is leap year or not if a year is divisible by 4 then its is leap year 
#but if the year is century year like 2000,1900,2100 then it must be divisible by 400
num=int(input("enter the number"))
if (num%4==0): 
   if (num%100==0):
      if (num%400==0):
         print("it is leap year")
      else:
         print("it is not leap year")
   else:
      print("it is leap year")
else: 
   print("is not leap year")