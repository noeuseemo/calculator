pr = input ("что делаем? (+, -, *, //,**, %)-  ")

a = int(input('введите число а- '))
b = int(input('введите число б- '))

if pr == '+':
    z = a+b
    print (f' {a}+{b}={z}')
    
elif pr == '-':
    v = a-b
    print (f'{a} + {b} = {v}' ) 

elif pr == '*':
    x = a*b
    print (f'{a} * {b} = {x}')

elif pr == '//':
    z = a//b
    print (f'{a}//{b}={z}')

elif pr == '**':
    g= a**b
    print (f'{a}**{b} = {g}')

elif pr == '%':
    h= (a*b)/100
    print (f'получится {h} рублей') 
    
else:
   print ("ошибка ввода")



     
