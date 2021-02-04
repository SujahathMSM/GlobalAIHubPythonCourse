#def prime():
#   i=2
#   while (i<100):
#       j=2
#       while (j <=(i/j)):
#           if not (i%j):break
#       if (j>i/j):print(i)
#       i=i+1
#prime()

def prime():                   # defining the function
    for num in range(0,100):   # checking the integers from 0 to 100
        if num>1:
            for i in range(2,num):  # checking the factors
                if num%i==0:
                    break
            else:
                print(num)    # if number has only two factors then print it
prime()