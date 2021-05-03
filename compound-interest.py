# capitalization per month
km = 10000
#period
t = 5
# start-up capital
p = 0
# target
goal = 500000

# annual interest
j = 0.07
# inflation
i = 0.06


# periodicity of replenishment
m = 12

#—————

# how much you need to top up per month,
# to achieve a goal in t years
a = goal * ((j-i)/m) * (1/( (1+((j-i)/m))**(m*t)-1 ) )
print (a)

print ("-")

# amount in years
p1 = p
for n in range(1, t+1):
    p1 = km * ( (1+(j-i)/m)**(m*n)-1 ) * m/(j-i)
    if p1<goal:
        print(int(p1))
    else:
        print(int(p1), n)