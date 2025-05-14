# Checking a Number is Even or Odd

def isEven(x):
    try:
        if x%2 == 0:
            return f"{x}: is Even"
        else:
            return f"{x} is Odd"
    except Exception as error:
        return f"Error: Please provide a valid Integer: {error}"
    
    
print(isEven(100)) # Even
print(isEven(101)) # Odd
print(isEven("a12")) # Error