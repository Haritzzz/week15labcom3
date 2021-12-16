x = str(input("Input Date (DD-MM-YYYY) : "))
Date1 = {"January":["1"],"Febuary":["2"],"March":["3"],"April":["4"],"May":["5"],"June":["6"],"July":["7"],"August":["8"]
,"September":["9"]}
Date2 = {"October":["10"],"November":["11"],"December":["12"]}
a=x[0:2]
b=x[6:10]
if x[3]=="0":
    for i in Date1:
        for j in Date1[i]:
            if x[4]==j:
                y=i
                print("{}-{}-{}".format(a,y,b))
else:
    for i in Date2:
        for j in Date2[i]:
            if x[3:5]==j:
                z=i
                print("{}-{}-{}".format(a,z,b))
