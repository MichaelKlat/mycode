#!/usr/bin/env python3
name_input = input("What is your name? ")
day_input = input("What day of the week is it? ")
print("Hello, " + name_input, "Happy " + day_input)
print("Hello, ", name_input, "! Happy", day_input,"!",sep=" ") # Print Objects
print("Hello, " + name_input + "! Happy " + day_input + "!") # Concatenation
print(f"Hello, {name_input}! Happy {day_input}!") # F-String
