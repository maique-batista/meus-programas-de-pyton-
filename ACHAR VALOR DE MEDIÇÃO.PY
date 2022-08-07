     
n = int(input())
v = []
aux = []
aux1 = []
for i in range(n):
    v.append(int(input()))
for j in range(n):
    aux.append(v.count(v[j]))
    aux1.append(v[j])
a = max(aux)
p = []
for m in range(len(aux)):
    if a == aux[m]:
        p.append(aux1[m])
            
print(max(p))
print(a)
        

