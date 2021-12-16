'''filename = "Test01.txt"
f=open(filename,'w')
myInput=""
myInput=input("Enter Line ('\\' to exit) : ")
while myInput != "\\":
    print(myInput)
    f.write(f"{myInput}\n")
    myInput=input("Enter Line ('\\' to exit) : ")
print("End")
f.close()'''

'''f=open("Test02.txt","w",encoding="UTF-8")
f.write("ant:มด\n")
f.write("bat:ค้างคาว\n")
f.write("bin:ถังขยะ\n")
f.write("cat:แมว\n")
f.write("rat:หนู\n")
f.write("zebra:ม้าลาย\n")
f.write("zoo:สวนสัตว์\n")
f.close()'''

f=open("Test02.txt","r",encoding="UTF-8")
dict={}
for i in f:
    i=i.replace('\n','')
    a=i.split(":")
    if len(a)==2:
        dict.update({a[0]:a[1]})
f.close
print(dict)