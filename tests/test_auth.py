def test_get_token(client, user):
    response = client.post(
        '/token',
        data={'username': user.email, 'password': user.clean_password},
    )
    token = response.json()

    assert response.status_code == 200
    assert 'access_token' in token
    assert 'token_type' in token


def test_get_token_raise_error_if_emails_doesnt_exists(client, user):
    response = client.post(
        '/token',
        data={
            'username': 'email_qualquer@email.com',
            'password': user.clean_password,
        },
    )

    assert response.status_code == 400
    assert response.json()['detail'] == 'Incorrect email or password'


def test_get_token_raise_error_if_password_not_match(client, user):
    response = client.post(
        '/token',
        data={
            'username': user.email,
            'password': user.clean_password + 'a',
        },
    )

    assert response.status_code == 400
    assert response.json()['detail'] == 'Incorrect email or password'
