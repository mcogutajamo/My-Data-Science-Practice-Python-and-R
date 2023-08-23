# Writing Functions in Python-Own Practice

# Simple Squaring function

def square (value):
  new_value=value**2
  print (new_value)

square (10)
square(5000000000) 

#Returning a value from the function using return
def square (value):
  """Return the square of a value."""
  new_value=value**2
  return new_value

num=square(10000)

print(num)

###Multiple function parameters
def raise_to_power (value1, value2):
  """Raise value 1 to the power of value 2-This section is called a DocString"""
  new_value=value1**value2
  return new_value

result= raise_to_power (10,3)
print(result)

#Returning multiple values

def raise_both (value1, value2):
  """Raise value 1 to the power of value 2
  and vice versa"""
  
  new_value1=value1**value2
  new_value2=value2**value1
  
  new_tuple=(new_value1, new_value2)
    
  return new_tuple

result= raise_both (10,3)
print(result)

###Nested functions##

#Long version

def mod2plus5 (x1,x2,x3):
  """Returns the remainder plus 5 of three values-THis the long version."""
  new_x1 = x1 % 2 + 5
  new_x2 = x2 % 2 + 5
  new_x3 = x3 % 2 + 5
  return (new_x1, new_x2, new_x3)

result= mod2plus5 (1,2,3)
print (result)

##Shorter/nested version
def mod2plus5 (x1, x2, x3):
  """Returns the remainder plus 5 of three values"""
  def inner (x):
    """Returns the remainder plus 5 of three values"""
    return x % 2 + 5
  return (inner(x1), inner(x2), inner(x3))

print(mod2plus5(1,2,3))

#Second example of nested functions
def raise_val (n):
  """Return the inner function"""
  def inner(x):
    """Raise x to the power of n."""
    raised=x ** n
    return raised
  return inner

square=raise_val(2)
cube=raise_val(3)

print (square(2), cube(4))























