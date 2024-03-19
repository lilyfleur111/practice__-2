def sum_of_multiples(num1, num2, limit):
    total_sum = 0
    for i in range(1, limit):
        if i % num1 == 0 or i % num2 == 0:
            total_sum += i
    return total_sum

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
limit = int(input("Enter the limit: "))

result = sum_of_multiples(num1, num2, limit)
print(f"The sum of multiples of {num1} or {num2} up to {limit} is {result}.")