n = int(input().strip())

if n % 2 == 1: # if n is odd
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5: # if n is even and in the range of 2 to 5 (inclusive)
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20: # if n is even and in the range of 6 to 20 (inclusive)
    print("Weird")
elif n % 2 == 0 and n > 20: # if n is even and greater than 20
    print("Not Weird")