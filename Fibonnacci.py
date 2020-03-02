
memo = {0: 0, 1: 1}


def fib(n):
    if n < 0:
        raise ValueError
    if n not in memo:
        memo[n] = fib(n-1) + fib(n-2)
    return memo[n]


def num_char(n):
    fib_len = len(str(memo[n]))
    n_len = len(str(n+1))
    return fib_len + n_len + 2


N = int(input("Enter a number of Fibonnacci numbers: ")) - 1
fib(N)
max_char = num_char(N)
print("Fibonacci sequance:")
for k, v in memo.items():
    diff = max_char - num_char(k)
    print(str(k+1) + ": " + " "*diff + str(v))
