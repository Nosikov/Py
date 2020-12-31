
s=0; i=1
while i<= 1000 and s< 5:
    s+=1/i
    i+=1
print(s)

print("++++++++++++++++++++")
s=0; i=-5
while i<= 4:
    i += 1
    if i==0: continue
    print(i)
    s+=1/i
print(s)

print("----------------------")
for x in 1, 5, 2, 4:
    print(x**2)
print("=======================")
for x in range(1,5,1):
    print(x)
print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
for x in range(5):
    print(x)
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
s=0
for i in range (1, 1000, 1):
    s+= 1/i
print(s)
print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
k=0.5; b=2
lst = [0, 0.1, 0.2, 0.3, 0.4, 0.5]
for x in lst:
    print(x*k+b)
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
msg="Hello World!"
for x in msg:
    print(x)
print("###########################")
A= [[1,2,3],[4,5,6]]
N=2; M=3
for i in range(N):
    for j in range (M):
        print(A[i][j], end='')
    print()
print("|||||||||||||||||||||||||||")
s=0; M=10; N=5
for i in range(1, N+1):
    for j in range(1, M + 1):
        s+=i*j
print(s)




