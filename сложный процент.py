#цель
goal = 500000
#период
t = 5
#стартовый капитал
st = 5000

#годовые проценты
j = 0.04
#инфляция
i = 0.08

#периодичность пополнений в год
m = 12

#—————

#сколько нужно инвестировать в месяц,
#что бы достичь goal за t лет
a = (goal-st) * ((j-i)/m) * (1/( (1+((j-i)/m))**(m*t)-1 ) )
print (int(a), '\n')

#сумма через года
km = a
for n in range(1, t+1):
    p = st + km * ( (1+(j-i)/m)**(m*n)-1 ) * m/(j-i)
    if n==1 or n%5==0:
        print(int(p), n)
    elif p<goal:
        print(int(p))
    else:
        print(int(p), n)
