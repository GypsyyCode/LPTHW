# variable dec and init
types_of_people= 10
# var dec + init with a string containig another var
x = f"There are {types_of_people} types of people"
# stirng var
binary = "binary"
# string var
do_not = "don't"
# var dec + init with a string containig another var
y = f"Those who know {binary} and those who {do_not}"

# print var
print(x)
# print var
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"
#format after creation
print(joke_evaluation.format(hilarious))

w = "This is the left side if ..."
e = "a string with right side"
# concat string vars
print(w+e)
