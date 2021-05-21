import math


# Example of list comprehension
numbers1 = [2 ** i for i in range(1, 6)]
# print(numbers)


# List comprehension with if statement
numbers2 = [49, 64, 81, 100, 121]
numbers2_c = [math.sqrt(i) for i in numbers2 if i % 2 == 0]
# print(numbers2_c)


# List comprehension with TWO if statements
num_list = [y for y in range(100) if y % 2 == 0 if y % 5 == 0]
# print(num_list)


# List comprehension with if else statements
numbers3 = [49, 64, 81, 100, 121]
numbers3_c = [math.sqrt(i) if i % 2 == 0 else i ** 5 for i in numbers3]
# print(numbers3_c)


# List comprehension with TWO 'if else' statements
numbers4 = [49, 64, 81, 100, 121]
numbers4_c = [
    math.sqrt(i) if i % 2 == 0 else i ** 5 if i % 7 == 0 else i + 10000
    for i in numbers4
]
# print(numbers4_c)


# Multiple loops in list comprehension
team1 = ["Janet", "Arya", "Mary"]
team2 = ["Evan", "Jake", "Randy"]
team_c = [(x, y) for x in team1 for y in team2]
# print(team_c)


# Transpose of Matrix using Nested Loops
transposed = []
matrix = [[1, 2, 3, 4], [4, 5, 6, 8]]

for i in range(len(matrix[0])):
    transposed_row = []

    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

transposed_c = [[row[i] for row in matrix] for i in range(len(matrix[0]))]

# print(transposed)
# print(transposed_c)

# Set comprehension
word = "programming"
spelling = {letter for letter in word}
# print(spelling)


# Dictionary comprehension
nums = [1, 2, 3, 4, 5]
square = dict()
for num in nums:
    square[num] = num ** 2

square_c = {num: num ** 2 for num in nums}
print(square_c)


# Dictionary comprehension (one more example)
# Increase the price of items for those that are more then $2
old_price = {"milk": 1.02, "coffee": 2.5, "bread": 2.5}
new_price = dict()
for sku, price in old_price.items():
    if price > 2:
        new_price[sku] = price * 1.5
    else:
        new_price[sku] = price

new_price_c = {
    sku: price * 1.5 if price > 2 else price for sku, price in old_price.items()
}

# print(new_price_c)
