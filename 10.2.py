def number_of_paths(n, m):
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    dp[0][0] = 1

    for i in range(n):
        for j in range(m):
            if i + 1 <= n:
                dp[i + 1][j] += dp[i][j]
            if j + 1 <= m:
                dp[i][j + 1] += dp[i][j]

    print (dp)
    return dp[n - 1][m - 1]


if __name__ == '__main__':
    n = int(input('Введіть кількість рядків: '))
    m = int(input('Введіть кількість стовпців: '))
    print(f"Кількість шляхів у сітці {n}x{m}: {number_of_paths(n, m)}")
