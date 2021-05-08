# capitalization per month
km = 10000
#period
t = 5
# target
goal = 500000

# annual interest
j = 0.04
# inflation
i = 0.08


# periodicity of replenishment
m = 12

#—————

# how much you need to top up per month,
# to achieve a goal in t years
a = goal * ((j-i)/m) * (1/( (1+((j-i)/m))**(m*t)-1 ) )
print (int(a))

print ("-")

# amount in years
for n in range(1, t+1):
    p1 = km * ( (1+(j-i)/m)**(m*n)-1 ) * m/(j-i)
    if p1<goal:
        print(int(p1))
    else:
        print(int(p1), n)
