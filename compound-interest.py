# capitalization per month
#km = 10000
#period
t = 5
# target
goal = 500000
# start-up capital
st = 5000

# annual interest
j = 0.04
# inflation
i = 0.08


# periodicity of replenishment
m = 12

#—————

# how much you need to invest per month,
# to achieve a goal in t years
a = (goal-st) * ((j-i)/m) * (1/( (1+((j-i)/m))**(m*t)-1 ) )
print (int(a))

print ("-")
# amount in years
km = a
for n in range(1, t+1):
    p = st + km * ( (1+(j-i)/m)**(m*n)-1 ) * m/(j-i)
    if n==1 or n%5==0:
        print(int(p), n)
    elif p<goal:
        print(int(p))
    else:
        print(int(p), n)
