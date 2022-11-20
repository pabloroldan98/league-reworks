import itertools

from MCKP import multipleChoiceKnapsack


def best_teams(players_list, formations, budget):
    # players_by_group = sorted(players_list, key=lambda x: x.get_group())

    for formation in formations:
        player_values, player_prices, player_positions, player_comb_indexes = players_preproc(players_list, formation)

        print(player_values)
        print(player_prices)
        print(player_positions)
        print(player_comb_indexes)
        print(len(player_values))

        score, comb_result_indexes = multipleChoiceKnapsack(budget, player_prices, player_values, player_positions)

        result_indexes = []
        for comb_index in comb_result_indexes:
            for win_i in player_comb_indexes[comb_index]:
                result_indexes.append(win_i)

        result = []
        for res_index in result_indexes:
            result.append(players_list[res_index])

        print("With formation " + str(formation) + ": " + str(score))
        for best_player in result:
            print(best_player)
        print()
        print()


def players_preproc(players_list, formation):
    max_gk = 1
    max_def = formation[0]
    max_mid = formation[1]
    max_att = formation[2]

    gk_values, gk_weights, gk_indexes = generate_group(players_list, "GK")
    gk_comb_values, gk_comb_weights, gk_comb_groups, gk_comb_indexes = group_preproc(gk_values, gk_weights, 0, gk_indexes, max_gk)

    def_values, def_weights, def_indexes = generate_group(players_list, "DEF")
    def_comb_values, def_comb_weights, def_comb_groups, def_comb_indexes = group_preproc(def_values, def_weights, 1, def_indexes, max_def)

    mid_values, mid_weights, mid_indexes = generate_group(players_list, "MID")
    mid_comb_values, mid_comb_weights, mid_comb_groups, mid_comb_indexes = group_preproc(mid_values, mid_weights, 2, mid_indexes, max_mid)

    att_values, att_weights, att_indexes = generate_group(players_list, "ATT")
    att_comb_values, att_comb_weights, att_comb_groups, att_comb_indexes = group_preproc(att_weights, att_weights, 3, att_indexes, max_att)

    result_comb_values = gk_comb_values + def_comb_values + mid_comb_values + att_comb_values
    result_comb_weights = gk_comb_weights + def_comb_weights + mid_comb_weights + att_comb_weights
    result_comb_groups = gk_comb_groups + def_comb_groups + mid_comb_groups + att_comb_groups
    result_comb_indexes = gk_comb_indexes + def_comb_indexes + mid_comb_indexes + att_comb_indexes

    return result_comb_values, result_comb_weights, result_comb_groups, result_comb_indexes


def generate_group(full_list, group):
    group_values = []
    group_weights = []
    group_indexes = []
    for i, item in enumerate(full_list):
        if item.position == group:
            group_values.append(item.value)
            group_weights.append(item.price)
            group_indexes.append(i)
    return group_values, group_weights, group_indexes


def group_preproc(group_values, group_weights, group, initial_indexes, r):
    comb_values = list(itertools.combinations(group_values, r))
    comb_weights = list(itertools.combinations(group_weights, r))
    comb_indexes = list(itertools.combinations(initial_indexes, r))

    group_comb_values = []
    for value_combinations in comb_values:
        values_added = sum(list(value_combinations))
        group_comb_values.append(values_added)

    group_comb_weights = []
    for weight_combinations in comb_weights:
        weights_added = sum(list(weight_combinations))
        group_comb_weights.append(weights_added)

    group_array = [group for _ in range(len(group_comb_values))]

    return group_comb_values, group_comb_weights, group_array, comb_indexes


