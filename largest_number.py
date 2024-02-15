numbers_list = list()
print("Enter 10 Values\n")
for i in range(10):
    entry = int(input(f"Value {i+1}:\n"))
    numbers_list.append(entry)
max = 0
for number in numbers_list:
    if max < number:
        max = number
print('Largest number is: ',max)