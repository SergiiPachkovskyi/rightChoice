from app import app


def base_test(url, get=True):
    app.testing = True
    client = app.test_client()
    if get:
        response = client.get(url)
        assert response.status_code == 200
    else:
        response = client.post(url)
        assert response.status_code == 302


def test_base_route():
    base_test('/')


def test_home():
    base_test('/home')


def test_alternatives_input_get():
    base_test('/alternatives_input')


def test_alternatives_input_post():
    base_test('/alternatives_input', get=False)


def test_categories_input_get():
    base_test('/categories_input')


def test_categories_input_post():
    base_test('/categories_input', get=False)


def test_accordance_input_get():
    base_test('/accordance_input')


def test_accordance_input_post():
    base_test('/accordance_input', get=False)
