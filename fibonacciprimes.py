# below function from 
# https://stackoverflow.com/questions/15347174/python-finding-prime-factors
def largest_prime_factor(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n

print("Prime factors of solution to Fibonacci recurrence with various initial conditions, we assume F(0)=a and F(1)=b and F(n+1)=F(n-1)+F(n) \n")
print("-------------------------------------------------------------------------------------------------------------------------------------")
def fib_to(n,a,b):
	fibs = [a, b]
	for i in range(2, n+1):
		fibs.append(fibs[-1] + fibs[-2])
	return fibs

def primefacs(n,a,b):
	return map(largest_prime_factor, fib_to(n,a,b))

i=0
j=0
while(i<10):
	while(j<10):
		print("a="+str(i)+",b="+str(j)+"prime factors:")
		print(primefacs(30,i,j))
		j+=1
	if(j==10):
		j=0
	i+=1
