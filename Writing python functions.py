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



























