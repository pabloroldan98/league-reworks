# Source: https://gist.github.com/USM-F/1287f512de4ffb2fb852e98be1ac271d

# groups is list of integers in ascending order without gaps

def getRow(lists, row):
    res = []
    for l in lists:
        for i in range(len(l)):
            if i == row:
                res.append(l[i])
    return res


def multipleChoiceKnapsack(W, weights, values, groups):
    n = len(values)
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]

    for w in range(W + 1):
        for i in range(n + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif weights[i - 1] <= w:
                sub_max = 0
                prev_group = groups[i - 1] - 1
                sub_K = getRow(K, w - weights[i - 1])
                for j in range(n + 1):
                    if groups[j - 1] == prev_group and sub_K[j] > sub_max:
                        sub_max = sub_K[j]
                K[i][w] = max(sub_max + values[i - 1], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    # stores the result of Knapsack
    res = K[n][W]
    sol = []

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
            sol.append(i - 1)
            print(i - 1)

            # Since this weight is included
            # its value is deducted
            res = res - values[i - 1]
            w = w - weights[i - 1]

    return K[n][W], sol


# Example
# values = [60, 100, 120]
# weights = [10, 20, 30]
# groups = [0, 0, 1]
# W = 50
# print(multipleChoiceKnapsack(W, weights, values, groups))  # 220
