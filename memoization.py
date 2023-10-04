# memoization
memo = {}


def memo_me(n):
    if n in memo.keys():
        print("memoized!")
        return memo[n]
    else:
        value = n * n
        memo[n] = value
        return value


if __name__ == '__main__':
    for i in range(10):
        print(memo_me(i))
    for i in range(10):
        print(memo_me(i))
