l1=[1,2,2,8]
l2=[2,4,6,12]
s=1
m=1
def nu_de():
    for i in l1:
        s=i
        s=s*i
    for j in l2:
        m=j
        m=m*j
    return s/m
print(nu_de())
