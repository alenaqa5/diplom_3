import pytest
from selenium import webdriver
import data
import requests
from helpers.payloads import UserPayloads
from helpers.endpoints import Endpoints


@pytest.fixture
def driver(request):
    browser, url = request.param
    if request.param == 'firefox':
        browser = webdriver.Firefox()
    elif request.param == 'chrome':
        browser = webdriver.Chrome()
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get(data.URLS[url])
    yield browser
    browser.quit()

@pytest.fixture()
def create_user():
    user = requests.post(url=Endpoints.register, json=UserPayloads.create_user)
    token = user.json().get("accessToken")
    yield token
    requests.delete(url=Endpoints.delete_user, headers={'Authorization': f'Bearer{token}'})
