import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_post_returns_expected_fields():
    response = requests.get(f"{BASE_URL}/posts/1", timeout=10)
    assert response.status_code == 200
    payload = response.json()
    assert payload["id"] == 1
    assert isinstance(payload["title"], str) and payload["title"]
    assert isinstance(payload["body"], str)


def test_get_posts_returns_collection():
    response = requests.get(f"{BASE_URL}/posts", timeout=10)
    assert response.status_code == 200
    payload = response.json()
    assert isinstance(payload, list)
    assert len(payload) > 0
    assert all("id" in post and "title" in post for post in payload[:5])


def test_create_post_returns_created_payload():
    data = {"title": "QA automation test", "body": "Isolated test payload", "userId": 1}
    response = requests.post(f"{BASE_URL}/posts", json=data, timeout=10)
    assert response.status_code == 201
    payload = response.json()
    assert payload["title"] == data["title"]
    assert payload["body"] == data["body"]
    assert payload["userId"] == data["userId"]
    assert "id" in payload
