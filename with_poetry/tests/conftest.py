import base64
import os
import pytest
from dotenv import load_dotenv
from with_poetry.testrail_tests.model import attach
from with_poetry.utils.base_session import BaseSession
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene.support.shared import browser


load_dotenv()
user = os.getenv('USER')
user_unregistered = os.getenv('USER_UNREGISTERED')
password = os.getenv('PASSWORD')
password_incorrect = os.getenv('PASSWORD_INCORRECT')
url_api= os.getenv('URL_API')
url_ui = os.getenv('URL_UI')
name = os.getenv('NAME')
DEFAULT_BROWSER_VERSION = "100.0"
login_senenoid = os.getenv('LOGIN_SELENOID')
password_senenoid = os.getenv('PASSWORD_SELENOID')


def pytest_addoption(parser):
    parser.addoption(
        '--browser_version',
        default='100.0'
    )


@pytest.fixture(scope='function')
def browser_management(request):
    browser_version = request.config.getoption('--browser_version')
    browser_version = browser_version if browser_version != "" else DEFAULT_BROWSER_VERSION
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": '100.0',
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    # options.capabilities.update(selenoid_capabilities)
    # driver = webdriver.Remote(
    #     command_executor=f"https://{login_senenoid}:{password_senenoid}@selenoid.autotests.cloud/wd/hub",
    #     options=options
    # )
    # browser.config.driver = driver
    #
    # yield browser
    #
    # attach.add_html(browser)
    # attach.add_screenshot(browser)
    # attach.add_logs(browser)
    # attach.add_video(browser)
    # browser.quit()


@pytest.fixture(scope='session', autouse=True)
def testrail_session():
    return BaseSession(base_url=url_api)


@pytest.fixture(scope='session', autouse=True)
def aunthatification():
    auth = str(
        base64.b64encode(
            bytes('%s:%s' % (user, password), 'utf-8')
            ),
            'ascii'
        ).strip()
    return auth


@pytest.fixture(scope='function', autouse=True)
def delete_project_before(testrail_session, aunthatification):
    response_select = testrail_session.get(url=f'/get_projects',
                           headers={'Authorization': 'Basic ' + aunthatification})

    if response_select.json()['projects'] != []:
        for i in response_select.json()['projects']:
            testrail_session.post(url=f"/delete_project/{i['id']}",
                          headers={'Authorization': 'Basic ' + aunthatification, 'Content-Type': 'application/json'})


@pytest.fixture(scope='function', autouse=True)
def delete_project_later(testrail_session, aunthatification):

    yield

    response_select = testrail_session.get(url=f'/get_projects',
                           headers={'Authorization': 'Basic ' + aunthatification})

    if response_select.json()['projects'] != []:
        for i in response_select.json()['projects']:
            testrail_session.post(url=f"/delete_project/{i['id']}",
                          headers={'Authorization': 'Basic ' + aunthatification, 'Content-Type': 'application/json'})






