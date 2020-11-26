#Taking Inputs
n = (input("Enter a Number: "))
#Creating empty variables
l = []
#Processing
for i in range(0,len(n)+1):
    n = int(n)
    s = n % 10
    l.append(int(s))
    n = (n-s)/10
b = sum(l)
#Giving Outputs
print("The sum of digits is %d."%(b))
