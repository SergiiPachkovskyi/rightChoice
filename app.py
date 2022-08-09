from flask import Flask, render_template, request, redirect

from utils import get_cat_compare_data, get_alt_compare_by_cat_list, get_global_priorities_data, get_charts_data

app = Flask(__name__)

ALTERNATIVES_LIST = list()
CATEGORIES_NAMES_LIST = list()
CATEGORIES_VALUES_LIST = list()
ACCORDANCE_ALT_DICT = dict()
ACCORDANCE_CAT_DICT = dict()


@app.route('/')
@app.route('/home')
def index():
    """
    Function for render index.html
    :template: index.html
    """

    return render_template('index.html')


@app.route('/alternatives_input', methods=['POST', 'GET'])
def alternatives_input():
    """
    Function for render alternatives_input.html or redirect to categories_input
    :template: alternatives_input.html
    """

    if request.method == 'POST':
        global ALTERNATIVES_LIST
        ALTERNATIVES_LIST.clear()
        count = 1
        for i in request.form.to_dict().items():
            if i[0].startswith('category'):
                pass
            else:
                ALTERNATIVES_LIST.append({count: i[1]})
                count += 1
        return redirect('/categories_input')
    else:
        return render_template('alternatives_input.html')


@app.route('/categories_input', methods=['POST', 'GET'])
def categories_input():
    """
    Function for render categories_input.html or redirect to accordance_input
    :template: categories_input.html
    """

    if request.method == 'POST':
        global CATEGORIES_NAMES_LIST, CATEGORIES_VALUES_LIST
        CATEGORIES_NAMES_LIST.clear()
        CATEGORIES_VALUES_LIST.clear()
        count = 1
        for i in request.form.to_dict().items():
            if i[0].startswith('category'):
                CATEGORIES_NAMES_LIST.append({count: i[1]})
            else:
                CATEGORIES_VALUES_LIST.append({count: i[1]})
                count += 1
        return redirect('/accordance_input')
    else:
        return render_template('categories_input.html')


@app.route('/accordance_input', methods=['POST', 'GET'])
def accordance_input():
    """
    Function for render accordance_input.html or redirect to result
    :template: accordance_input.html
    """

    if request.method == 'POST':
        global ACCORDANCE_ALT_DICT, ACCORDANCE_CAT_DICT
        ACCORDANCE_ALT_DICT.clear()
        ACCORDANCE_CAT_DICT.clear()
        for i in request.form.to_dict().items():
            alt_cat = i[0].split('_')

            if alt_cat[0] in ACCORDANCE_ALT_DICT.keys():
                ACCORDANCE_ALT_DICT[alt_cat[0]].append({alt_cat[1]: i[1]})
            else:
                ACCORDANCE_ALT_DICT.update({alt_cat[0]: [{alt_cat[1]: i[1]}]})

            if alt_cat[1] in ACCORDANCE_CAT_DICT.keys():
                ACCORDANCE_CAT_DICT[alt_cat[1]].append({alt_cat[0]: i[1]})
            else:
                ACCORDANCE_CAT_DICT.update({alt_cat[1]: [{alt_cat[0]: i[1]}]})
        return redirect('/result')
    else:
        global ALTERNATIVES_LIST, CATEGORIES_NAMES_LIST, CATEGORIES_VALUES_LIST
        return render_template('accordance_input.html', alternatives=ALTERNATIVES_LIST,
                               categories_names=CATEGORIES_NAMES_LIST, categories_values=CATEGORIES_VALUES_LIST,
                               rows=[i for i in range(1, len(ALTERNATIVES_LIST)+1)],
                               columns=[i for i in range(1, len(CATEGORIES_NAMES_LIST)+1)])


@app.route('/result')
def result():
    """
    Function for render result.html
    :template: result.html
    """

    global ACCORDANCE_CAT_DICT, CATEGORIES_VALUES_LIST

    alt_numbers = [i for i in range(1, len(ALTERNATIVES_LIST) + 1)]
    cat_numbers = [i for i in range(1, len(CATEGORIES_NAMES_LIST) + 1)]

    cat_compare_data = get_cat_compare_data(CATEGORIES_VALUES_LIST, cat_numbers)

    cat_alpha_list = cat_compare_data['cat_alpha_list']
    max_cat = cat_compare_data['max_cat']
    cat_max_alpha = cat_compare_data['cat_max_alpha']
    iy = cat_compare_data['iy']

    alt_compare_list = get_alt_compare_by_cat_list(ACCORDANCE_ALT_DICT, cat_numbers, alt_numbers)

    global_priorities_data = get_global_priorities_data(cat_alpha_list, alt_compare_list, cat_numbers, alt_numbers)

    global_priorities_list = global_priorities_data['global_priorities_list']
    max_priority = global_priorities_data['max_priority']
    max_priority_number = global_priorities_data['max_priority_number']

    charts_data = get_charts_data(ALTERNATIVES_LIST, global_priorities_list, alt_numbers)

    return render_template('result.html', alternatives=ALTERNATIVES_LIST, alt_number=alt_numbers,
                           categories_names=CATEGORIES_NAMES_LIST,
                           categories_values=CATEGORIES_VALUES_LIST, cat_number=cat_numbers,
                           accordance_alt=ACCORDANCE_ALT_DICT, accordance_cat=ACCORDANCE_CAT_DICT,
                           cats_alpha_list=cat_alpha_list, cat_max_alpha=cat_max_alpha, max_cat=max_cat,
                           iy=iy, values_alt=alt_compare_list,
                           global_priorities_list=global_priorities_list,
                           max_priority=max_priority, max_priority_number=max_priority_number,
                           charts_data=charts_data)


if __name__ == '__main__':
    app.run(debug=True)
