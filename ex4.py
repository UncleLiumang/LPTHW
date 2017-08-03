# assign cars.
cars = 100
# assign space_in_a_car.
space_in_a_car = 4.0
# assign drivers.
drivers = 30
# assign passengers.
passengers = 90
# assign cars_not_driven.
cars_not_driven = cars - drivers
# assign cars_driven.
cars_driven = drivers
# assign carpool_capacity.
carpool_capacity = cars_driven * space_in_a_car
# assign average_passengers_per_car.
average_passengers_per_car = passengers / cars_driven

# print number of available cars.
print "There are", cars, "cars available."
# print number of available drivers.
print "There are only", drivers, "drivers available."
# print number of empty cars today.
print "There will be", cars_not_driven, "empty cars today."
# print number of passengers to carpool today.
print "We have", passengers, "to carpool today."
# print number of passengers per car.
print "We need to put about", average_passengers_per_car, "in each car."
