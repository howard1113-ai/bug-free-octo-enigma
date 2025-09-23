N = int(input("Enter a number: "))

even_sum = 0

for i in range(1, N + 1):
    if i % 2 == 0:
        print(f"{i} is even")
        even_sum += i
    else:
        print(f"{i} is odd")

print(f"The sum of all even numbers up to {N} is {even_sum}")