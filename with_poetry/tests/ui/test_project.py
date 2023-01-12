import allure
from allure_commons.types import Severity
from with_poetry.testrail_tests.model.applicationmanager import app
from with_poetry.tests.conftest import user, url_ui, password, name, user_unregistered, password_incorrect


@allure.tag("ui")
@allure.label('owner', 'Elena')
@allure.feature('Ui')
@allure.severity(Severity.CRITICAL)
@allure.title('Add project')
def test_add_project_ui(delete_project_before, browser_management):
    with allure.step("Authorization"):
        app.auth.open_authorization_page(url_ui)
        app.auth.set_login_email(user)
        app.auth.set_password(password)
        app.auth.submit_auht()

    with allure.step('Create project'):
        app.add.add_new_project()
        app.add.set_name_project(name)
        app.add.add_announcement_project('Description for project')
        app.add.choice_show_announcement()
        app.add.choice_suites_model_multiple()
        app.add.confirming_create_project()

    with allure.step('Check create project'):
        app.add.checking_project_creation(name)
