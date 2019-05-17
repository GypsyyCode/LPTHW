# cars equal 100 Int
cars = 100
# spac in a car is float 4.0
space_in_a_car = 4
# drivers quals 30
drivers = 30
# passengers shoudt be 90
passengers = 90
# cars_not_driven equals the value of cars 10 minus the value of drivers 30  -20
cars_not_driven = cars -drivers
# cars_driven gets the value of drivers
cars_driven = drivers
# carpool_capacity gets the value of cars_drive (30) times space_in_a_car (4.0) = 120
carpool_capacity = cars_driven * space_in_a_car
# average_passengers_per_car gets the value of passengers (90) dividet by cars_driven (30) = 3
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available")
print("Ther are only", drivers, "drivers available")
print("There will be", cars_not_driven, "empty cars today")
print("We can transport", carpool_capacity, "people today")
print("We have", passengers, "to carpool today.")
print("We neet to put about", average_passengers_per_car, "in each car.")


####
# Traceback (most recent call last):
#    File "ex4.py", line 8, in <module>
#       average_passengers_per_car = car_pool_capacity / passenger
# NameError: name 'car_pool_capacity' is not defined

## Explaination
# In the file ext4.py on line 8 is an error that the variable car_pool_capacity
# is not defined because the cariable is name carpool_capacity!
