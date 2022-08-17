#Cac ham su dung trong bai
def songuyento(n):
    dem = 0
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                dem += 1
        if dem == 0:
            return True
        return False
    return False

def chinhphuong(n):
    for i in range(1,n):
        if i*i == n:
            return True
    return False

def tachso(n):
    s = []
    while n > 0:
        s.append(n % 10)
        n = n // 10
    return s

def giaithua(n):
    for i in range(1,n):
        n *= i
    return n

def ucln(a,b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

def sohoanhao(n):
    for i in range (len(n)-1):
        if n[i] == n[i-1]:
            return True
        return False

def soxenkechanle(n):
    for i in range(len(n)-1):
        if n[i] % 2 == 0:
            if n[i+1] % 2 != 0:
                return True
            return False
        elif n[i] % 2 != 0:
            if n[i+1] % 2 == 0:
                return True
            return False

def sodaonguoc(a,b):
    for i in range(len(a)):
        if a[i] == b[-i]:
            return True

def xenkechanle2so(a,b):
    if a % 2 == 0:
        if b % 2 == 0:
            return False
        return True
    elif a % 2 != 0:
        if b % 2 != 0:
            return False
        return True

#                                                              Bai Lam
#Cau 1
a,b = map(int, input("Nhap a va b: "))
print(a+b)

#Cau 2.1: a,b la so le
a,b = map(int, input("Nhap a va b la so le: ").split())
while a or b % 2 == 0:
    print("Nhap sai")
    a,b = map(int, input("Nhap a va b la so le: ").split())
print(a+b)

#Cau 2.1: a,b la so chan
a,b = map(int, input("Nhap a va b la so chan: ").split())
while a or b % 2 != 0:
    print("Nhap sai")
    a,b = map(int, input("Nhap a va b la so chan: ").split())
print(a+b)

#Cau 2.3: a,b la so nguyen to

a,b = map(int, input("Nhap a va b la so nguyen to: ").split())
while songuyento(a) == False or songuyento(b) == False:
    print("Nhap sai")
    a,b = map(int, input("Nhap a va b la so nguyen to: ").split())
print(a+b)

#Cau 2.4: a,b la so chinh phuong
a,b = map(int, input("Nhap a va b la so chinh phuong: ").split())
while chinhphuong(a) == False or chinhphuong(b) == False:
    print("Nhap sai")
    a,b = map(int, input("Nhap a va b la so chinh phuong: ").split())
print(a+b)

#Cau 2.5: a,b co UCLN khac 1
a,b = map(int, input("Nhap a va b co uoc chung khac 1: ").split())
while ucln(a,b) == 1:
    print("Nhap sai")
    a,b = map(int, input("Nhap a va b co uoc chung khac 1: ").split())
print(a+b)

#Cau 2.6: a,b la 2 so chia het cho nhau
a,b = map(int, input("Nhap a va b la 2 so chia het cho nhau: ").split())
while a % b != 0 or b % a != 0:
    print("Nhap sai")
    a,b = map(int, input("Nhap a va b la 2 so chia het cho nhau: ").split())
print(a+b)

#Cau 2.7: a,b la 2 so khong chia het cho nhau
a,b = map(int, input("Nhap a va b la 2 so khong chia het cho nhau: ").split())
while a % b == 0 or b % a == 0:
    print("Nhap sai")
    a,b = map(int, input("Nhap a va b la 2 so khong chia het cho nhau: ").split())
print(a+b)

#Cau 2.8: a,b la 2 so dao nguoc cua nhau
a,b = map(int, input("Nhap a va b la 2 số đảo ngược của nhau: ").split())
while sodaonguoc(tachso(a),tachso(b)) == False:
    print("Nhap sai")
    a,b = map(int, input("Nhap a va b la 2 số đảo ngược của nhau: ").split())
print(a+b)

#Cau 2.9: a,b la 2 so cach nhau n don vi
n = int(input("Nhap n: "))
a,b = map(int, input(f"Nhap a va b la 2 so cach nhau {n} don vi: ").split())
if a < b:
    while a + n != b:
        print("Nhap sai")
        a,b = map(int, input(f"Nhap a va b la 2 so cach nhau {n} don vi: ").split())
    print(a+b)
else:
    while b + n != a:
        print("Nhap sai")
        a,b = map(int, input(f"Nhap a va b la 2 so cach nhau {n} don vi: ").split())
    print(a+b)

#Cau 2.10: Tong a+b la so nguyen to
a,b = map(int, input("Nhap a va b: ").split())
s = a + b
while songuyento(s) == False:
    print("Nhap sai")
    a,b = map(int, input("Nhap a va b: ").split())
    s = a + b
print(s)

#Cau 2.11: Tong a+b la so chinh phuong
a,b = map(int, input("Nhap a va b: ").split())
s = a + b
while chinhphuong(s) == False:
    print("Nhap sai")
    a,b = map(int, input("Nhap a va b: ").split())
    s = a + b
print(s)

#Cau 2.12: a,b la so hoan hao
a,b = map(int, input("Nhap a va b la 2 so hoan hao: ").split())
while sohoanhao(tachso(a)) == False or sohoanhao(tachso(b)) == False:
    print("Nhap sai")
    a,b = map(int, input("Nhap a va b la so hoan hao: ").split())
print(a+b)

#Cau 2.13: a! + b!
a,b = map(int, input("Nhap a va b: ").split())
print(giaithua(a) + giaithua(b))

#Cau 2.14: a,b la so xen ke chan le
a,b = map(int, input("Nhap a va b la so xen ke chan le: ").split())
while soxenkechanle(a) == False or soxenkechanle(b) == False:
    print("Nhap sai")
    a,b = map(int, input("Nhap a va b la so xen ke chan le: ").split())
print(a+b)

#Cau 3:
print(input("Nhap chuoi: ").replace(" ","--"))

#Cau 4:
n = int(input("Nhap n he thap phan: "))
for i in range (len(tachso(n))):
    print(n % 8,end = "")
    n = n // 8

#Cau 5.1: n la so le
n = int(input("Nhap n la so le he thap phan: "))
while n % 2 == 0:
    print("Nhap sai")
    n = int(input("Nhap n la so le he thap phan: "))
for i in range (len(tachso(n))):
    print(n % 8,end = "")
    n = n // 8

#Cau 5.2: n la so chan
n = int(input("Nhap n la so chan he thap phan: "))
while n % 2 != 0:
    print("Nhap sai")
    n = int(input("Nhap n la so chan he thap phan: "))
for i in range (len(tachso(n))):
    print(n % 8,end = "")
    n = n // 8

#Cau 5.3: n la so nguyen to
n = int(input("Nhap n la so nguyen to he thap phan: "))
while songuyento(n) == False:
    print("Nhap sai")
    n = int(input("Nhap n la so nguyen to he thap phan: "))
for i in range (len(tachso(n))):
    print(n % 8,end = "")
    n = n // 8

#Cau 5.4: n la so chinh phuong
n = int(input("Nhap n la so chinh phuong he thap phan: "))
while chinhphuong(n) == False:
    print("Nhap sai")
    n = int(input("Nhap n la so chinh phuong he thap phan: "))
for i in range (len(tachso(n))):
    print(n % 8,end = "")
    n = n // 8

#Cau 5.5: n la so hoan hao
n = int(input("Nhap n la so hoan hao he thap phan: "))
while sohoanhao(tachso(n)) == False:
    print("Nhap sai")
    n = int(input("Nhap n la so hoan hao he thap phan: "))
for i in range (len(tachso(n))):
    print(n % 8,end = "")
    n = n // 8

#Cau 5.6: n!
n = int(input("Nhap n la thap phan: "))
print(giaithua(n))
for i in range (len(tachso(n))):
    print(n % 8,end = "")
    n = n // 8

#Cau 5.7: n la so xen ke chan le
n = int(input("Nhap n la so xen ke chan le he thap phan: "))
while soxenkechanle(tachso(n)) == False:
    print("Nhap sai")
    n = int(input("Nhap n la so xen ke chan le he thap phan: "))
for i in range (len(tachso(n))):
    print(n % 8,end = "")
    n = n // 8

#Cau 6
a = float(input("Nhap a: "))
b = int(input("Nhap so chu so thap phan sau dau , : "))
print(round(a,b))

#Cau 7:

#Cau 8:
print(sum(list(map(int, input("Nhap day so: ").split()))))

#Cau 9.1: Day so le
n = list(map(int, input("Nhap day so: ").split()))
for i in n:
    while i % 2 == 0:
        print("Nhap sai")
        n = list(map(int, input("Nhap day so: ").split()))
print(sum(n))

#Cau 9.2: Day so chan
n = list(map(int, input("Nhap day so: ").split()))
for i in n:
    while i % 2 != 0:
        print("Nhap sai")
        n = list(map(int, input("Nhap day so: ").split()))
print(sum(n))

#Cau 9.3: Day so nguyen to
n = list(map(int, input("Nhap day so: ").split()))
for i in n:
    while songuyento(i) == False:
        print("Nhap sai")
        n = list(map(int, input("Nhap day so: ").split()))
print(sum(n))

#Cau 9.4: Day so chinh phuong
n = list(map(int, input("Nhap day so: ").split()))
for i in n:
    while chinhphuong(i) == False:
        print("Nhap sai")
        n = list(map(int, input("Nhap day so: ").split()))
print(sum(n))

#Cau 9.5: Day so xen ke chan le
n = list(map(int, input("Nhap day so xen ke chan le: ").split()))
for i in range(0,len(n)-1):
    while xenkechanle2so(n[i],n[i+1]) == False:
        print("Nhap sai")
        n = list(map(int, input("Nhap day so: ").split()))
print(sum(n))

#Cau 9.6: Day so co ucln
n = list(map(int, input("Nhap day so: ").split()))
for i in range(0,len(n)-1):
    while ucln(n[i],n[i+1]) == 1:
        print("Nhap sai")
        n = list(map(int, input("Nhap day so: ").split()))
print(sum(n))

#Cau 10:
