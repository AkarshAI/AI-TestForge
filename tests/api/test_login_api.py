import pytest


@pytest.mark.api
@pytest.mark.smoke
@pytest.mark.parametrize(
    "username,password,role",
    [
        ("qa_user", "qa_password", "tester"),
        ("admin", "admin_password", "admin"),
    ],
)
def test_login_api(api_client, username, password, role):
    token = api_client.login(username, password)
    assert token.startswith("token_")

    profile = api_client.get_user_profile(token)
    assert profile["username"] == username
    assert profile["role"] == role
    assert profile["base_url"].startswith("https://")
