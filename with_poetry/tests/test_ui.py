import allure
from allure_commons.types import Severity
from with_poetry.testrail_tests.model.application_manager import app
from with_poetry.tests.conftest import user, url_ui, password, name


@allure.tag("ui")
@allure.label('owner', 'Elena')
@allure.feature('ui')
@allure.story('Add and delete project')
@allure.severity(Severity.CRITICAL)
@allure.title('Add and delete project')
def test_add_and_delete_project_ui(delete_project, browser_management):
    with allure.step("Authorization"):
        app.auth.open_authorization_pege(url_ui)
        app.auth.set_login_email(user)
        app.auth.set_password(password)
        app.auth.submit()

    with allure.step('Create project'):
        app.add.new_project()
        app.add.neme_project(name)
        app.add.announcement_project('Description for project')
        app.add.show_announcement()
        app.add.suites_model_multiple()
        app.add.confirm()

    with allure.step('Check create project'):
        app.add.create_check(name)

    with allure.step('Settings navigation'):
        app.settings.navigation()
        app.settings.project()
        app.settings.select_deleting()

    with allure.step('Delete project'):
        app.confirm.delete()
        app.confirm.submit()
        app.confirm.lack_project()



