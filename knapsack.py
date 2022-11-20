# Python3 code for Dynamic Programming
# based solution for 0-1 Knapsack problem

# Prints the items which are put in a
# knapsack of capacity W
def printknapSack(W, wt, val, n):
    K = [[0 for w in range(W + 1)]
         for i in range(n + 1)]

    # Build table K[][] in bottom
    # up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1]
                              + K[i - 1][w - wt[i - 1]],
                              K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    # stores the result of Knapsack
    res = K[n][W]
    print(res)

    w = W
    for i in range(n, 0, -1):
        if res <= 0:
            break
        # either the result comes from the
        # top (K[i-1][w]) or from (val[i-1]
        # + K[i-1] [w-wt[i-1]]) as in Knapsack
        # table. If it comes from the latter
        # one/ it means the item is included.
        if res == K[i - 1][w]:
            continue
        else:

            # This item is included.
            print(wt[i - 1])
            print(i - 1)

            # Since this weight is included
            # its value is deducted
            res = res - val[i - 1]
            w = w - wt[i - 1]


# Driver code
val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)

printknapSack(W, wt, val, n)


# This code is contributed by Aryan Garg.


# Source: https://stackoverflow.com/questions/45891999/knapsack-multiple-constraints

def knapsack2(n, weight, count, values, weights):
    dp = [[[0] * (weight + 1) for _ in range(n + 1)] for _ in range(count + 1)]
    for z in range(1, count + 1):
        for y in range(1, n + 1):
            for x in range(weight + 1):
                if weights[y - 1] <= x:
                    dp[z][y][x] = max(dp[z][y - 1][x],
                                      dp[z - 1][y - 1][x - weights[y - 1]] +
                                      values[y - 1])
                else:
                    dp[z][y][x] = dp[z][y - 1][x]

    return dp[-1][-1][-1]


w = 5
k = 3
values = [1, 2, 3, 2, 2]
weights = [4, 5, 1, 1, 1]
n = len(values)

no_limit_fmt = 'Max value for weight limit {}, no item limit: {}'
limit_fmt = 'Max value for weight limit {}, item limit {}: {}'

print(limit_fmt.format(w, k, knapsack2(n, w, k, values, weights)))


def knapsack3(n, weight, values, weights, count):
    K = [[[0 for _ in range(count + 1)]
           for _ in range(weight + 1)]
          for _ in range(n + 1)]
    for c in range(1, count + 1):
        for i in range(1, n + 1):
            for w in range(weight + 1):
                if w == 0 or i == 0 or c == 0:
                    K[i][w][c] = 0
                elif weights[i - 1] <= w:
                    K[i][w][c] = max(K[i - 1][w][c],
                                      K[i - 1][w - weights[i - 1]][c - 1] +
                                      values[i - 1])
                else:
                    K[i][w][c] = K[i - 1][w][c]

    # stores the result of Knapsack
    res = K[-1][-1][-1]
    # print(res)

    w = weight
    c = count
    for i in range(n, 0, -1):
        if res <= 0:
            break
        # either the result comes from the
        # top (K[i-1][w]) or from (val[i-1]
        # + K[i-1] [w-wt[i-1]]) as in Knapsack
        # table. If it comes from the latter
        # one/ it means the item is included.
        if res == K[i - 1][w][c]:
            continue
        else:

            # This item is included.
            print("Item in pos: " + str(i - 1))

            # Since this weight is included
            # its value is deducted
            res = res - values[i - 1]
            w = w - weights[i - 1]
            c = c - 1

    return K[-1][-1][-1]


w = 5
k = 2
values = [1, 2, 3, 2, 2]
weights = [4, 5, 1, 1, 1]
n = len(values)

no_limit_fmt = 'Max value for weight limit {}, no item limit: {}'
limit_fmt = 'Max value for weight limit {}, item limit {}: {}'

print(limit_fmt.format(w, k, knapsack3(n, w, values, weights, k)))
