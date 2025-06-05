marks = int(input ("ENter your grade :"))

if  ( marks > 100 ):
    print ("Invalid marks")
elif( marks >= 90 ):
    print ("Grade_A")
elif( marks >=80 & marks < 90):
    print ("Grade_B")
elif( marks >= 70 & marks < 80):
    print ("Grade_B")
else :
    print ("Grade_D")