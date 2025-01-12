def fibonacci(x):
    y=[0,1]
    for i in range(2,x):
        z=y[-1]+y[-2]
        y.append(z)
    return y
x=int(input("Enter the number"))
print(fibonacci(x))