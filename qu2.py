# strong password
password=input("enter a password:")
if len(password)>=6:
 if"$"in password or"#"in password or "@"in password:
   if"A"or"Z"in password:
     if"0"or"9"in password:
        print("strong password")
     else:
        print("weak password")
   else:  
       print("wrong password")
 else:
      print("wrong")
else:
    print("noting")
        