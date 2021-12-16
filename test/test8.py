f = open("text.txt","a",encoding="UTF-8")
while True :
    key=str(input("Enter string 'student ID:Name:Grade' ('/' to exit) : "))
    if key == '/':
        f.close()
        break
    f.write("\n"+str(key))
    print(f"Write {key} to file")
f = open("text.txt","r",encoding="UTF-8")    
while True :
    search = str(input("Enter ID to search ('/' to exit) : "))
    if search == '/':
        break
    for i in f.readlines():
        if search in i:
            data=i.split(":")
            print(f"student ID : {data[0]}")
            print(f"Name : {data[1]}")
            print(f"Grade : {data[2]}")
f.close()   
