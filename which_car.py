import sys

car1 = "MH abc"
car2 = "MH xyz"

print ("As we can see both car are same so To find our car ,we have to find with num plate")
find = input("should we ? Y/N? : ")
if find == "Y" or find == "y" :
    print("Yup , let's Find out!")
else :
    print("Then ! Walking back Home ? ")
    sys.exit()

num = input("Tell our car num : ")
if num == car1 :
    print ("we got it ! , Its first one ..")
elif num == car2 :
    print("That's the second car. It's not ours.")
else :
    print("Dude ! Its not a car num !!")