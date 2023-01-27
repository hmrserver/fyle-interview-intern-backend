def test_user_model(database, user_model):
    user_details = {
        'username': 'test',
        'email': 'testuser@test.fylehq.com'
    }
    user = user_model(**user_details)

    database.session.add(user)
    database.session.commit()
    assert user.username == 'test'
    assert user.email == 'testuser@test.fylehq.com'
    assert user == user_model.get_by_id(user.id)
    assert user == user_model.get_by_email(user.email)