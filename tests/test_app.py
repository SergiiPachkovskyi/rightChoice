from flask import Flask


def test_base_route():
    app_ = Flask(__name__)
    client = app_.test_client()

    url = '/'

    response = client.get(url)
    assert response.status_code == 200
