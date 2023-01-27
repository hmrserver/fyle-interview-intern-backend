#Description: This file contains all the test cases for the global API

#Used to test whether Index API is working or not
def test_get_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json['status'] == 'ready'

#Used to test whether invalid path returning proper error
def test_get_404(client):
    response = client.get('/404')
    assert response.status_code == 404
    assert response.json['error'] == 'NotFound'

#Used to test whether header without principal is returning proper error
def test_get_principal_unauthorized(client):
    response = client.get(
        '/student/assignments'
    )

    assert response.status_code == 401

    data = response.json
    assert data['error'] == 'FyleError'
    assert data['message'] == 'principal not found'