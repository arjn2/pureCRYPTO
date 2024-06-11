def cyclesub(g,p):
    flag=True
    gp=[]
    i=0
    while flag!=False:
        k=pow(g,i,p)
        if(gp.count(k)==0):
            gp.append(k)
        else:
            flag=False
        i+=1
    return sorted(gp)

def gcd(a,b):
  r=1
  if(a<0 or b<0):
    print("Invalid numbers:",a,b)
    return "ERR"

  elif(a==0 or b==0):
    return max(a,b)

  else:
    if(a<b):
      a,b=b,a
    while r!=0:
      r=a%b
      a=b
      b=r
  return a

def generate_z(n):

    z=[]
    for i in range(1,n):
        if gcd(n,i)==1:
            z.append(i)
    return z

def find_g(p):
    g_list=[]
    z=generate_z(p)
    for i in range(2,p):
        k=cyclesub(i,p)
        if(k==z):
            g_list.append(i)
    return g_list

def A_pub(g,a,p):
    A=pow(g,a,p)
    return A

def encrypt(g,p,A,m):
    r=list(range(1,p-2))
    k=r[5]
    c1=pow(g,k,p)
    c2=(m*(A**k))%p
    return c1,c2

def prime(n):
  k=True
  if(n<2):
    k=False
  else:
    for i in range(2,(n//2+1)):
      if(n%i==0):
        k=False
  return k
    


p=int(input("Enter a prime: "))
if prime(p):
    g=find_g(p)[0]
    a=int(input("Enter private key: "))
    m=int(input("Enter the message: "))

    A=A_pub(g,a,p)
    cipher=encrypt(g,p,A,m)
else:
    print("Enter prime number")

print(f"pvt key: {a} \n msg: {m} \n public key ,generator ,prime: ({g},{A},{p}) \n cipher: {cipher} ")


