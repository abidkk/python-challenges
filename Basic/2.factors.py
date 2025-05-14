# getting all factors

def factors():
    numList = []
    x = int(input("Please enter a valid Integer: "))
    for i in range(1,x):
        if x%i==0:
            numList.append(i)
      
    return f"Factors of {x} : {numList}"

print(factors())
print(factors())
print(factors())