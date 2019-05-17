# ex5.py

name = 'Zed a. Shaw'
age = 35
height = 74 #inches
weight = 180 #lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall. That are about {round(height / 0.39370)} cm.")
print(f"He's {weight} pounds heavy. That are about {round(weight / 2.2046)} kg.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.");
print(f"His teeth are usally {teeth} depending on the coffee.")

# this lin is tricky, try to get i exacly right
total = age + height + weight
print(f"If i add {age}, {height} and {weight} I get {total}.")
