# Fibonacci:
# F=0 for  n = 0
# F=1 for n = 1
# F(n-1)+F(n-2) n>1

arr_fib = [0, 1]

print("*" * 20)
print("Hello, this program help you to find Fibonacci Sequence for selected number")
n = int(input("Select number that's greater or equal 0: "))

if n < 0:
	print("Wrong number")
if n == 0:
    print(0)
if n == 1:
    print(1)
else:
    for i in range(2, n+1):
        fib = arr_fib[i-1] + arr_fib[i-2]
        arr_fib.append(fib)

print(f"Fibonacci value for your number is {fib}")
