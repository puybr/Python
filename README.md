# 🐍 Python

Created by _Guido van Rossum_, and released in 1991.

```py
# This is a comment
print("Hello, Friend!")
```

## Data Types
+ Text Type:	`str`
   + Concatenation of Strings: `FullName = Name + " " + Surname`
   + `"Python"` **Forward Indexing**: `0`, `1`, `2`, `3`, `4`, `5`
   + `"Python"` **Backward Indexing**: `-6`, `-5`, `-4`, `-3`, `-2`, `-1`
   + `len()`: `print(len("Hello World!"))`
   + Slice a string: `print(veryLongWord[0:5])`
   + String manipulation and functions: `astring.upper()`, `astring.lower()`, `astring.replace("$", " ")`, `astring.strip('*')`
+ Numeric Types:	`int`, `float`, `complex`
+ Sequence Types:	`list`, `tuple`, `range`
+ Mapping Type:	`dict`
+ Set Types:	`set`, `frozenset`
+ Boolean Type:	`bool`
+ Binary Types:	`bytes`, `bytearray`, `memoryview`

## Variables
A variable is created from the moment you assign a value to it

```py
x = 5
y = "String"
print(x)
print(y)
```

Variables to hold user input: `name = input("Enter your name: ")`

```py
name = input("What is your name?")
print("Hello, " + name + "!")
```

> There are 4 built-in data types used to store _collections_ of data: **List**, **Tuple**, **Set**, & **Dictionary**.

## Lists
List items are ordered, changeable, and allow duplicate values.

```py
mylist = ["orange", "pink", "green"]
```

## Tuples
A tuple is a collection of data which is ordered, unchangeable, and allows duplicate values.

```py
mytuple = ("orange", "pink", "green")
```

## Sets
Set items are unordered, unchangeable, and **do not** allow duplicate values.

```py
myset = {"orange", "pink", "green"}
```

## Dictionaries
Dictionary items are ordered, changeable, and does not allow duplicates. They are presented in `key:value` pairs, and can be referred to by using the key name.

```py
mydict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
```

> Note: You can use LISTS as ARRAYS, however, to work with arrays in Python you will have to import a library, like the `NumPy` library.

## Casting
Taking different types of data and converting them into different types for different purposes.
+ `str()` - converts an argument to a string
+ `int()` - converts an argument to an integer
+ `float()` - converts an argument to a float

```py
number = int(input("Please enter a number"))
answer = number * 10
print(str(number) + " x 10 = " + str(answer))
```
> The `print()` function can only work with string arguments. By default anything entered into an input is a string.

## Numbers

| Arithmetic Operations | Python Symbol |
|-----------------------|---------------|
| Addition              | +             |
| Subtraction           | -             |
| Multiplication        | *             |
| Division              | /             |
| Modulus               | %             |
