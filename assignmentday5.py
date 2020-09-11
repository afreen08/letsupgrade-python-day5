#sub list in list
def a(y,z):
    common=0
    for value in y:
        if value in z:
            common=1
    if(not common):
       print("its gone")
    else:
        print("match")
a([1,11,2,3,16,3,9,8],[3,1,9])


#captalize
s=["hi whatsapp"]
t=map(lambda x:x.title(),s)
u=list(s)
print(u)


#prime
def prime(n):
    count=0
    for i in range(2,n):
        if(n%i==0):
            count+=1
    if(count==2):
        print("prime")
    else:
        print("not prime")
l=list(range(1,2501))        
print(l)
q=filter(prime,1)
print(list(q))
