file_names = ["document1.txt", "image1.jpg", "document2.txt", "image2.jpg"]

for file_name in file_names:
    print(file_name)

greeting = 'Hello, World!'
for char in greeting:
    print(char)

greeting = 'Hello, World!'
count = 0
for char in greeting:
    if char == 'o':
        # count = count + 1
        count += 1

print(count)

students = ["Alice", "Bob", "Charlie", "David"]

for student in students:
    print(student)
    for letter in student:
        print(letter)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

for num in numbers:
    # Skip odd numbers
    if num % 2 != 0:
        continue

    # Break the loop if the number is 10
    if num == 10:
        print("Found 10, breaking the loop!")
        break

    print(f"Even number: {num}")
