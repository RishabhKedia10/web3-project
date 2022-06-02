import hashlib
import timeit

start = timeit.default_timer()
s=input("Enter String: ")
t=s
num=0
s+=str(num)
hash=hashlib.sha256(s.encode()).hexdigest()

while(int(hash,16)>=int('00000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF',16)):
    s=t
    num=num+1
    s+=str(num)
    hash=hashlib.sha256(s.encode()).hexdigest()
    
stop = timeit.default_timer()
print('nonce = ', num)

print('time = ', stop - start)
