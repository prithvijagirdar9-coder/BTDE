n = int(input("Enter a number: "))

n = abs(n)

digit_sum = 0
while n > 0:
    digit_sum += n % 10
    n //= 10

print("Sum of digits: ",digit_sum)