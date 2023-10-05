m=[]#animalstick
f=[]
l=0
x=input()
n=x.split()
for i in range(len(n)):
    m.append(int(n[i]))
for i in range(0,3):
    c=0
    for j in range(len(n)):
         f.append(int(n[j]))  
    h=len(f)
    for j in range(len(m)):
         if(m[i]==m[j]):
            c=c+1
            f[j]=0
    for j in range(h):
        if(f[j]=='0'):
            f.pop(f[j])
    if(c==4 or c>4):
        if(f[0]==f[1]):
           print('elephant')
           l=1
           break
        else:
           print('bear')
           l=1
           break
if(l!=1):
    print('alien')
