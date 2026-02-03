integer_input = int(input("Enter an integer: "))
float_input = float(input("Enter a float: "))
string_input = input("Enter a string: ")

print(type(integer_input))
print(type(float_input))
print(type(string_input))

text = "123"
number = int(text)
number_float = float(number)

print(type(number))
print(type(number_float))

person = {
    "name": "Bob",
    "age": 30
}

print(person["name"])

my_set = {1, 2, 3}
my_set.add(4)
my_set.remove(2)
print(3 in my_set)
