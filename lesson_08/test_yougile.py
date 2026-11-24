import requests

BASE_URL = "https://ru.yougile.com"
KEY = "ВСТАВЬТЕ ВАШ KEY"
HEADERS = {
    "Authorization": f"Bearer {KEY}",
    "Content-Type": "application/json"
}


def test_create_project_positive():
    resp = requests.post(
        BASE_URL + '/api-v2/projects',
        headers=HEADERS,
        json={"title": "Новый проект"}
                   )
    assert resp.status_code == 201


def test_get_project_positive():
    resp = requests.post(
        BASE_URL + '/api-v2/projects',
        headers=HEADERS,
        json={"title": "Новый проект"}
    )
    project_id = resp.json()['id']

    resp = requests.get(
        BASE_URL + f'/api-v2/projects/{project_id}',
        headers=HEADERS
    )
    assert resp.status_code == 200
    assert resp.json()['id'] == project_id


def test_update_project_positive():
    resp = requests.post(
        BASE_URL + '/api-v2/projects',
        headers=HEADERS,
        json={"title": "Новый проект"}
    )
    project_id = resp.json()['id']

    resp = requests.put(
        BASE_URL + f'/api-v2/projects/{project_id}',
        headers=HEADERS,
        json={"title": "Обновлённый проект"}
    )
    assert resp.status_code == 200


def test_create_project_negative():
    resp = requests.post(
        BASE_URL + '/api-v2/projects',
        headers=HEADERS,
        json={}
                   )
    assert resp.status_code == 400


def test_get_project_negative():
    resp = requests.get(
        BASE_URL + f'/api-v2/projects/{1223}',
        headers=HEADERS
    )
    assert resp.status_code == 404


def test_update_project_negative():
    resp = requests.put(
        BASE_URL + f'/api-v2/projects/{234}',
        headers=HEADERS,
        json={"title": "Обновлённый проект"}
    )
    assert resp.status_code == 404
