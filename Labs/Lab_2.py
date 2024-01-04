# Lab 2
def q1():
    x1=0
    x2=0
    for i in range(1,10):
        print(f"Current Number {x1} Previous Number  {x2}  Sum:  {x1+x2}")
        x1=x2
        x2+=1

def q2():
    str="Zulfiqar Ali"
    for i in range(0,len(str),2):
        print(str[i])
        
def q3(n):
    
    stringname="HeyThere"
    if n <= len(stringname):
        for i in range(n,len(stringname)):
            print(stringname[i])
    else:
        print("Error! N > String")
        
def q4():
    arr=[1,2,3,4,5,1]
    n=len(arr)
    if arr[0] == arr[n-1]:
        print(True)
    else:
        print(False)

def q5(list1,list2):
    list3=[]
    for i in list1:
        if i % 2 == 0:
            list3.append(i)
            
    for i in list2:
        if i % 2 != 0:
            list3.append(i)
    return list3

lista = [1,2,3,4,5]
listb = [6,7,8,9,10]
listc = q5(lista,listb)

def q8(s1,s2):
    s3=[]
    for i in range(0,int(len(s1)/2+1)):
        s3.append(s1[i])
    for i in range(0,int(len(s2))):
        s3.append(s2[i])
    for i in range(int(len(s1)/2+1),int(len(s1))):
        s3.append(s1[i])
    
    return s3
        
strr = q8("TeAmo","SarahYousaf")


