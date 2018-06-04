
passwd = 'admin'
if 'admin' == passwd:
    print("authenticated")
else:
    print("fatal error")


for x in range(1,101):
    print("fizz"[x%3*4::]+"buzz"[x%5*4::]or x)

for x in range(1,101):
    if x % 15 == 0:
        print('fuzzbuzz')
    elif x % 3 == 0:
        print('fuzz')
    elif x % 5 == 0:
        print('buzz')
    else:
        print(x)

list = []


while True:
    a = input()
    if a == 'exit':
        break
    else:
        list.append(a)
list.sort()
print(list)

