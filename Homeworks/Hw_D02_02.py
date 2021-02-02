n=int(input('Enter a number: '))  # get an integer from user
l=[i for i in range(n+1) if i%2==0]  # finding the even numbers and appending to a list
for j in l:
    print(j)                  #Extraxcting the even numbers 
