print("Hello")
my_var = 1
if my_var == 1:
    print(1)
    print(3)
    my_new_var = 3
elif my_var == 2:
    print(2)
else:
    print("apperò")

print("Cane")

# my comment
"""
multiline comment
"""

while not my_var == 10 and my_var < 20 or my_var > 20:
    print (my_var)
    my_var += 1

nums = range(10)  # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
nums = range(1, 10) # 1, 2, 3, 4, 5, 6, 7, 8, 9
nums = range(1, 10, 2) # 1, 3, 5, 7, 9

for num in nums:
    print(num)

my_strings = ["ciao", "come", "stai"]
for i in range(len(my_strings)):
    print(i)

