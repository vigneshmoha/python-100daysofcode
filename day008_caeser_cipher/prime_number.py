def isPrimeNumber(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

num = int(input("Enter a number: "))
if isPrimeNumber(num):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")