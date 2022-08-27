language=input("enter the language:")
if language=="english"or language=="hindhi":
   print("welcome to state bank of india\n swipe card")
   balance=5000
   print("choose your transction 1.balance equairy\n 2.withdraw\n 3.deposit\n 4.transfer\n 5.exit")
   transction=int(input("enter the transction"))
   if transction==1 or transction==2 or transction==3 or transction==4 or transction==5:
      atm_pin=int(input("enter the atm pin"))
      if atm_pin==1234:
         if transction==1:
            print("collect your balance\nthankyou for using me")
            print ("balance is:",balance)
         elif transction==2:
              amount=int(input("enter the amount"))
              total=balance-amount
              if amount<=balance:
                 print(total)
                 print("collect your cash\n thankyou for using me")
              else:
                 print("you have no balance")
         elif transction==3:
              deposite=int(input("enter the deposite amount"))
              total=balance+deposite
              if deposite>0:
                 print(total)
                 print("your deposite is successful\n thankyou for using me")
              else:
                 print("no deposit")
         elif transction==4:
              transfermoney=int(input("enter the transfer money"))
              total=balance-transfermoney
              if transfermoney>0:
                 print(total)
                 print("sucessfully transfer your money\n thankyou for using me")
              else:
                 print("please enter the avalid amount")
         else:
            print("wrong pin")
   elif transction==5:
       exit=input("if you want to exit")
       if exit=="yes": 
          print("exit")
       else:
          print("choose your transction")
else:
    print("language does not exit")
   
        
        
  