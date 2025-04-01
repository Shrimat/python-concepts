# A generator function, resulting in an iterator object uisng the yield keyword
def square_numbers_generator(nums):
    for i in nums:
        yield i * i


generator = square_numbers_generator([1, 2, 3, 4])

for num in generator:
    print(num)

# Generator does not hold all values in memory, it just gets the first one and stops at the first yield statement
# Understand how iterators and iterator objects work in Python

# Generator expressions
generator_exp = ((i*i) for i in [1, 2, 3, 4])

for num in generator_exp:
    print(num)