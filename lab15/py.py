
with open("example.txt", "w") as f:
    f.write("Hello World")
    f.write("Python makes handling easier")

with open("example.txt", "r") as f:
    contents = f.read()
    print(contents)

with open("example.txt", "r") as f:
    for line in f:
        print(line.strip(), end="")

with open("example.txt", "w") as f:
    f.write("\nThis line was added later.")

try:
    with open("example.txt", "x") as f:
        f.write("\nThis line was added later.")

except FileExistsError:
    print("File already exists")

with open("example.txt", "r") as f:
    for line in f:
        print(f"Processed line: {line.strip()}")

data =[
    ["Name", "Age", "City"],
    ["Alice", "32", "New-York"],
    ["Bob", "34", "New-York"],
    ["Luc", "21", "Washington"]
]

import csv 

with open("example.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(data)

with open("example.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)


with open("example.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(f"{row['Name']} is {row['Age']} years old and live in the {row['City']}")

new_data = [["David", 28, "San-Francisco"]]
with open("example.csv", "a", newline = '') as f:
    writer = csv.writer(f)
    writer.writerows(new_data)


filename = 'sample_text.txt'

content = """Hello, world!
This is a sample text file.
It contains multiple lines of text for testing file operations."""

with open(filename, 'w') as file:
    file.write(content)
print(f"Content has been written to {filename}")

with open(filename, 'r') as file:
    read_content = file. read ()


print("Content read from the file:")
print(read_content)

csv_filename = 'people.csv'

data = [
    ["Name", "Age", "City"],
    ["Alice", "30", "New York"],
    ["Bob", "25", "Los Angeles"],
    ["Charlie", "35", "Chicago"]
]

with open(csv_filename, 'w' , newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)

print(f"Data has been written to {csv_filename}")

print("Reading data from the CSV file:")
with open(csv_filename, 'r', newline="") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print (row)

filename = 'sample_text.txt'
additional_text = "\nThis line is appended to the file."

with open (filename, 'a') as file:
    file.write(additional_text)
print(f"Additional text has been appended to {filename}")

with open(filename, 'r') as file:
    updated_content = file. read ()
print("Updated content of the file:")
print(updated_content)