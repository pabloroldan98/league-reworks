
def best_squads(players_list, formations, budget):
    n = len(players_list)
    player_values = []
    player_prices = []
    player_positions = []
    for player in players_list:
        player_values.append(player.value)
        player_prices.append(player.price)
        if player.position == "GK":
            player_positions.append(0)
        elif player.position == "DEF":
            player_positions.append(1)
        elif player.position == "MID":
            player_positions.append(2)
        else:
            player_positions.append(3)

    for formation in formations:
        max_gk = 1
        max_def = formation[0]
        max_mid = formation[1]
        max_att = formation[2]

        score, result_indexes = group_knapsack(n, budget, player_values, player_prices, max_gk, max_def, max_mid, max_att, player_positions)

        result = []
        for res_index in result_indexes:
            result.append(players_list[res_index])

        print("With formation " + str(formation) + ": ")
        for best_player in result:
            print(best_player)
        print()
        print()



def group_knapsack(n, weight, values, weights, count_group_a, count_group_b, count_group_c, count_group_d, groups):
    K = [[[[[[0
        for _ in range(count_group_d + 1)]
        for _ in range(count_group_c + 1)]
        for _ in range(count_group_b + 1)]
        for _ in range(count_group_a + 1)]
        for _ in range(weight + 1)]
        for _ in range(n + 1)]
    for d in range(1, count_group_d + 1):
        for c in range(1, count_group_c + 1):
            for b in range(1, count_group_b + 1):
                for a in range(1, count_group_a + 1):
                    for i in range(1, n + 1):
                        for w in range(weight + 1):
                            if groups[i - 1] == 0:
                                added_weight_group = K[i - 1][w - weights[i - 1]][a - 1][b][c][d]
                                count_check = a - 1
                            elif groups[i - 1] == 1:
                                added_weight_group = K[i - 1][w - weights[i - 1]][a][b - 1][c][d]
                                count_check = b - 1
                            elif groups[i - 1] == 2:
                                added_weight_group = K[i - 1][w - weights[i - 1]][a][b][c - 1][d]
                                count_check = c - 1
                            else:
                                added_weight_group = K[i - 1][w - weights[i - 1]][a][b][c][d - 1]
                                count_check = d - 1

                            if i == 0 or w == 0 or (a == 0 and b == 0 and c == 0 and d == 0):
                                K[i][w][a][b][c][d] = 0
                            elif weights[i - 1] <= w and count_check >= 0:
                                K[i][w][a][b][c][d] = max(K[i - 1][w][a][b][c][d],
                                                  added_weight_group + values[i - 1])
                            else:
                                K[i][w][a][b][c][d] = K[i - 1][w][a][b][c][d]

    # stores the result of Knapsack
    res = K[-1][-1][-1][-1][-1][-1]
    # print(res)
    sol=[]

    w = weight
    a = count_group_a
    b = count_group_b
    c = count_group_c
    d = count_group_d
    for i in range(n, 0, -1):
        if res <= 0:
            break
        # either the result comes from the
        # top (K[i-1][w]) or from (val[i-1]
        # + K[i-1] [w-wt[i-1]]) as in Knapsack
        # table. If it comes from the latter
        # one/ it means the item is included.
        if res == K[i - 1][w][a][b][c][d]:
            continue
        else:

            # This item is included.
            sol.append(i - 1)
            # print("Item in pos: " + str(i - 1))

            # Since this weight is included
            # its value is deducted
            res = res - values[i - 1]
            w = w - weights[i - 1]
            if groups[i - 1] == 0:
                a = a - 1
            elif groups[i - 1] == 1:
                b = b - 1
            elif groups[i - 1] == 2:
                c = c - 1
            else:
                d = d - 1

    return K[-1][-1][-1][-1][-1][-1], sol


w = 5
k = 2
values = [1, 2, 3, 2, 2]
weights = [4, 5, 1, 1, 1]
n = len(values)

no_limit_fmt = 'Max value for weight limit {}, no item limit: {}'
limit_fmt = 'Max value for weight limit {}, item limit {}: {}'

print(limit_fmt.format(w, k, group_knapsack(n, w, values, weights, k)))
