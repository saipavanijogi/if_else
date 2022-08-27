beds=int(input("enter the beds:"))
girls=int(input("enter the girls:"))
if girls>beds:
    print("girls will go to anthor room")
elif beds>girls:
    print("beds go to anthor room ")
elif beds<10:
    print("we need more beds")
elif girls<10:
    print("we need more")
elif girls==beds:
    print("those are equal")
else:
  print("nothing")        