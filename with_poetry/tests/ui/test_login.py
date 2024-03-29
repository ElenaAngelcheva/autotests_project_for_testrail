import allure
from allure_commons.types import Severity
from with_poetry.testrail_tests.model.applicationmanager import app
from with_poetry.tests.conftest import user, url_ui, password, name, user_unregistered, password_incorrect


@allure.tag("ui")
@allure.label('owner', 'Elena')
@allure.feature('Ui')
@allure.severity(Severity.CRITICAL)
@allure.title('Authorization by registered user')
def test_authorization_by_registered_user(browser_management):
    with allure.step("Authorization"):
        app.auth.open_authorization_page(url_ui)
        app.auth.set_login_email(user)
        app.auth.set_password(password)
        app.auth.submit_auht()
    with allure.step("Result"):
        app.auth.checking_title()


@allure.tag("ui")
@allure.label('owner', 'Elena')
@allure.feature('Ui')
@allure.severity(Severity.CRITICAL)
@allure.title('Authorization by registered user with incorrect password')
def test_authorization_by_registered_user_with_incorrect_password(browser_management):
    with allure.step("Authorization"):
        app.auth.open_authorization_page(url_ui)
        app.auth.set_login_email(user)
        app.auth.set_password(password_incorrect)
        app.auth.submit_auht()
    with allure.step("Result"):
        app.auth.checking_loginpage_message_title()


@allure.tag("ui")
@allure.label('owner', 'Elena')
@allure.feature('Ui')
@allure.severity(Severity.CRITICAL)
@allure.title('Authorization by an unregistered user')
def test_authorization_by_an_unregistered_user(browser_management):
    with allure.step("Authorization"):
        app.auth.open_authorization_page(url_ui)
        app.auth.set_login_email(user_unregistered)
        app.auth.set_password(password)
        app.auth.submit_auht()
    with allure.step("Result"):
        app.auth.checking_loginpage_message_title()

