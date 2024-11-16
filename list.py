import random
numbers=list(range(1,11))
for i in numbers:
    print(i,end=" ")
numbers[4]=30
print(numbers)
random_number_from_the_numbers=random.choice(numbers)
print(random_number_from_the_numbers)

