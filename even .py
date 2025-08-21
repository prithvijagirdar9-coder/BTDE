N = int(input("Enter a positive integer: "))
if N > 0:
    for i in range(2, N + 1, 2):  
           print(i, end=' ')
else:
    print("Please enter a positive integer.")
