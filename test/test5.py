'''a = input("Enter Number : ")
if a=='1':
    print("one")
elif a=='2':
    print("two")
elif a=='3':
    print("three")
else:
    print("Other Number")'''

'''[a,b]=[int(tmp)for tmp in input("ป้อนตัวเลข 2 ชุด คั่นด้วยช่องระหว่าง : ").split()]
print(f"{a} < {b}")if a < b else print(f"{a} = {b}")if a==b else print ("{a} > {b}")'''

'''i=1
while True:
    i += 1
    if (i%2)==0:
        continue
    print(i)
    if i == 12:
        break
else:
    print("loop end")'''

'''step = input("Enter Step : ")
step = int(step)
for i in range (1,50,step):
    print(i)'''

'''x = "Hello"
def myfunc():
    x="good bye,"
    print(x + "your name.")
myfunc()
print(x + "your name")'''

x = "Hello"
print(x + "your name")
def myfunc():
    global x
    x="Good Bye,"
myfunc()
print(x + "your name")