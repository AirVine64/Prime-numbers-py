#Imports
import time

st = time.time()

#Variables
primes = []

#Main part
for i in range(1, 1000000, 2):
    z = 1
    for j  in range(2, i+1):
        if i % j == 0:
            z += 1
            if z == 3:
                break;
    if z == 2:
        primes.append(i);
print(primes)

et = time.time()
elapsed = et - st
print(f"Elapsed time: {elapsed}s")