# kadai_008
# import random module
import random

# set var from 100 to 0 randomly
var = random.randint(0,100)

print (var)
print (type(var))


if var % 3 == 0:
  print ("Fizz")

if var % 5 == 0:
  print ("Buzz")

if var % 15 == 0:
  print ("FizzBuzz")
