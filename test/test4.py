x = int(input("ใช้ไฟฟ้าไป : "))
n=x
price=0
if n<=50:
    price = n*2
    print("ใช้ไฟฟ้า {} หน่วย จะคิดเป็น = {}x2 = {}".format(x,n,price))
elif n<=100:
    n=n-50
    price = (50*2)+(n*3)
    print("ใช้ไฟฟ้า {} หน่วย จะคิดเป็น = (50x2)+({}x3) = {}".format(x,n,price))
elif n<=500:
    n=n-100
    price = (50*2)+(50*3)+(n*5)
    print("ใช้ไฟฟ้า {} หน่วย จะคิดเป็น = (50x2)+(50x3)+({}x5) = {}".format(x,n,price))
else:
    n=n-500
    price = (50*2)+(50*3)+(400*5)+(n*7)
    print("ใช้ไฟฟ้า {} หน่วย จะคิดเป็น = (50x2)+(50x3)+(400x5)+({}x7) = {}".format(x,n,price))