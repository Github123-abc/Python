# Method 2 : using min() & max() methods
#mylist=[20, 100, 20, 1, 10]
#print("smallest element is:", min(mylist))
#print("largest element is:", max(mylist))


#method 3 :

n1 = int (input("Enter the 1st number: "))
n2 = int (input("Enter the 2nd number: "))
n3 = int (input("Enter the 3rd number: "))
if (n1 > n2):
    if (n1 > n3):
        print ("1st number is the largest number")
    else:
        print ("3rd number is the largest number")
elif (n2 > n3):
    print ("2nd number is the largest number")
else:
    print ("3rd number is the largest number")




