from app import app


def base_get_test(url):
    app.testing = True
    client = app.test_client()
    response = client.get(url)
    assert response.status_code == 200


def test_base_route():
    base_get_test('/')


def test_home():
    base_get_test('/home')


def test_alternatives_input_get():
    base_get_test('/alternatives_input')


def test_categories_input_get():
    base_get_test('/categories_input')


def test_accordance_input_get():
    base_get_test('/accordance_input')

