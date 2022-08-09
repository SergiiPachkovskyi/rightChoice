import json
from decimal import Decimal
from math import log


def root(basis: int, power: int) -> float:
    """
    Function for calculate root
    :param basis: int
    :param power: int
    :return: float
    """

    if power == 1:
        return basis

    factorial = 1
    cur_power = 1
    sum = 0
    power_e = 1 / power * log(basis)

    for ii in range(1, 29):
        factorial = factorial * ii
        cur_power = cur_power * power_e
        sum = sum + cur_power/factorial

    return round(sum + 1, 3)


def get_cat_compare_data(categories: list, cat_numbers: list) -> dict:
    """
    Function for getting category comparison data
    :param categories: list
    :param cat_numbers: list
    :return: dict
    """

    cat_comparison_dict = dict()
    cat_alpha_list = list()
    for r in cat_numbers:
        cat_comparison_dict.update({'accordance' + str(r): {}})
        sum = 0
        for c in cat_numbers:
            cat_r = int(categories[r - 1].get(r))
            cat_c = int(categories[c - 1].get(c))
            if cat_r == cat_c:
                cat_comparison_dict['accordance' + str(r)] = {'accordance' + str(c): 1}
                sum += 1
            else:
                if cat_r > cat_c:
                    div = (cat_r - cat_c + 1) / 1
                    cat_comparison_dict['accordance' + str(r)] = {
                        'accordance' + str(c): div
                    }
                else:
                    div = 1 / (cat_c - cat_r + 1)
                    cat_comparison_dict['accordance' + str(r)] = {
                        'accordance' + str(c): 1 / (cat_c - cat_r + 1)
                    }
                sum += div
        cat_alpha_list.append(root(sum, len(cat_numbers)))

    cat_max_alpha = 0
    max_cat = 0
    for c in cat_numbers:
        if cat_alpha_list[c - 1] > cat_max_alpha:
            cat_max_alpha = cat_alpha_list[c - 1]
            max_cat = c

    iy = round((cat_max_alpha - len(cat_numbers)) / (len(cat_numbers) - 1), 3)

    return {'cat_comparison_dict': cat_comparison_dict, 'cat_alpha_list': cat_alpha_list,
            'cat_max_alpha': cat_max_alpha, 'max_cat': max_cat, 'iy': iy}


def get_alt_compare_by_cat_list(alternatives: dict, cat_numbers: list, alt_numbers: list) -> list:
    """
    Function for getting a list of comparison of alternatives by category
    :param alternatives: list
    :param cat_numbers: list
    :param alt_numbers: list
    :return: list
    """

    alt_compare_list = list()
    for cat in cat_numbers:
        alt_comparison_by_cat_dict = dict()
        alt_alpha_by_cat_list = list()
        for r in alt_numbers:
            alt_comparison_by_cat_dict.update({'alternative' + str(r): {}})
            sum = 0
            for c in alt_numbers:
                cat_r = int(alternatives['alternative' + str(r)][cat - 1]['category' + str(cat)])
                cat_c = int(alternatives['alternative' + str(c)][cat - 1]['category' + str(cat)])
                if cat_r == cat_c:
                    alt_comparison_by_cat_dict['alternative' + str(r)] = {'alternative' + str(c): 1}
                    sum += 1
                else:
                    if cat_r > cat_c:
                        div = (cat_r - cat_c + 1) / 1
                        alt_comparison_by_cat_dict['alternative' + str(r)] = {
                            'alternative' + str(c): div
                        }
                    else:
                        div = 1 / (cat_c - cat_r + 1)
                        alt_comparison_by_cat_dict['alternative' + str(r)] = {
                            'alternative' + str(c): 1 / (cat_c - cat_r + 1)
                        }
                    sum += div
            alt_alpha_by_cat_list.append(root(sum, len(alt_numbers)))

        max_alt = 0
        alt_max_alpha = 0
        for a in alt_numbers:
            if alt_alpha_by_cat_list[a - 1] > alt_max_alpha:
                alt_max_alpha = alt_alpha_by_cat_list[a - 1]
                max_alt = a

        iy_ = round((alt_max_alpha - len(alt_numbers)) / (len(alt_numbers) - 1), 3)

        alt_compare_list.append({'category' + str(cat): [{'alt_comparison_by_cat_dict': alt_comparison_by_cat_dict},
                                                         {'alt_alpha_by_cat_list': alt_alpha_by_cat_list},
                                                         {'alt_max_alpha': alt_max_alpha},
                                                         {'max_alt': max_alt},
                                                         {'iy': iy_}]})
    return alt_compare_list


def get_global_priorities_data(cat_alpha_list: list, alt_compare_list: list, cat_numbers: list, alt_numbers: list)\
        -> dict:
    """
    Function for getting global priorities data
    :param cat_alpha_list: list
    :param alt_compare_list: list
    :param cat_numbers: list
    :param alt_numbers: list
    :return: dict
    """

    global_priorities_list = list()
    for r in alt_numbers:
        alt_sum = 0
        for c in cat_numbers:
            alt_sum = round(alt_sum + alt_compare_list[c - 1]['category' + str(c)][1]['alt_alpha_by_cat_list'][r - 1]
                            * cat_alpha_list[c - 1], 3)
        global_priorities_list.append(alt_sum)

    max_priority = 0
    max_priority_number = 0
    for a in alt_numbers:
        if global_priorities_list[a - 1] > max_priority:
            max_priority_number = a
            max_priority = global_priorities_list[a - 1]

    return {'global_priorities_list': global_priorities_list, 'max_priority': max_priority, 'max_priority_number': max_priority_number}


def get_charts_data(alternatives: list, global_priorities_list: list, alt_numbers: list) -> str:
    """
    Function for getting charts data
    :param alternatives: list
    :param global_priorities_list: list
    :param alt_numbers: list
    :return: str
    """

    charts_data = dict()
    charts_data["charts_alternatives"] = dict()
    charts_data["charts_alternatives"]["priorities_list"] = [{'name': alternatives[i - 1][i],
                                                              'data': [global_priorities_list[i - 1]]}
                                                             for i in alt_numbers]

    def custom_serializer(obj):
        if isinstance(obj, Decimal):
            return float(obj)

    charts_data = json.dumps(charts_data, default=custom_serializer)

    return charts_data
