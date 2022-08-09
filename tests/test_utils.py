import pytest

import utils


@pytest.mark.parametrize("basis, power, expected_result", [(4, 2, 2),
                         (27, 3, 3),
                         (256, 4, 4)])
def test_root(basis, power, expected_result):
    assert utils.root(basis, power) == expected_result


@pytest.mark.parametrize("value1, value2, expected_result", [(1.5, 3, -0.75),
                         (2, 4, -0.667),
                         (2.449, 2, 0.449)])
def test_evaluate_iy(value1, value2, expected_result):
    assert utils.evaluate_iy(value1, value2) == expected_result


@pytest.mark.parametrize("values_list, numbers_list, expected_result",
                         [([1, 2, 3], [1, 2, 3], {'max_value': 3, 'max_number': 3})])
def test_get_max_value(values_list, numbers_list, expected_result):
    assert utils.get_max_value(values_list, numbers_list) == expected_result


@pytest.mark.parametrize("alternatives, global_priorities_list, alt_numbers, expected_result",
                         [([{1: 'a1'}, {2: 'a2'}], [1, 2], [1, 2],
                           '{"charts_alternatives": {"priorities_list":'
                           ' [{"name": "a1", "data": [1]}, {"name": "a2", "data": [2]}]}}')])
def test_get_charts_data(alternatives, global_priorities_list, alt_numbers, expected_result):
    assert utils.get_charts_data(alternatives, global_priorities_list, alt_numbers) == expected_result


@pytest.mark.parametrize("categories, cat_numbers, expected_result",
                         [([{1: '9'}, {2: '7'}, {3: '7'}], [1, 2, 3],
                           [1.913, 1.326, 1.326])])
def test_get_cat_compare_data(categories, cat_numbers, expected_result):
    assert utils.get_cat_compare_data(categories, cat_numbers)['cat_alpha_list'] == expected_result


@pytest.mark.parametrize("alternatives, cat_numbers, alt_numbers, expected_result",
                         [({'alternative1': [{'category1': '7'}, {'category2': '7'}, {'category3': '7'}],
                            'alternative2': [{'category1': '3'}, {'category2': '9'}, {'category3': '9'}]},
                           [1, 2, 3], [1, 2],
                           [2.449, 1.095])])
def test_get_alt_compare_by_cat_list(alternatives, cat_numbers, alt_numbers, expected_result):
    assert utils.get_alt_compare_by_cat_list(alternatives, cat_numbers,
                                             alt_numbers)[0]['category1'][0]['alt_alpha_by_cat_list'] == expected_result


@pytest.mark.parametrize("cat_alpha_list, alt_compare_list, cat_numbers, alt_numbers, expected_result",
                         [([1.913, 1.326, 1.326],
                           [{'category1': [{'alt_alpha_by_cat_list': [2.449, 1.095]}, {'alt_max_alpha': 2.449},
                                           {'max_alt': 1}, {'iy': 0.449}]},
                            {'category2': [{'alt_alpha_by_cat_list': [1.155, 2.0]},
                                           {'alt_max_alpha': 2.0}, {'max_alt': 2}, {'iy': 0.0}]},
                            {'category3': [{'alt_alpha_by_cat_list': [1.155, 2.0]}, {'alt_max_alpha': 2.0},
                                           {'max_alt': 2}, {'iy': 0.0}]}],
                           [1, 2, 3], [1, 2],
                           [7.749, 7.399])])
def test_get_global_priorities_data(cat_alpha_list, alt_compare_list, cat_numbers, alt_numbers, expected_result):
    assert utils.get_global_priorities_data(cat_alpha_list, alt_compare_list, cat_numbers
                                            , alt_numbers)['global_priorities_list'] == expected_result
