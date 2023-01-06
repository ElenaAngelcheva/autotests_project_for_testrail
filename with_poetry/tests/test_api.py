import allure
import pytest
from allure_commons.types import Severity
from pytest_voluptuous import S
from with_poetry.Schema.testrail import CreatePprojectSchema


@allure.tag("api")
@allure.label('owner', 'Elena')
@allure.feature('API')
@allure.story('Working with the project')
@allure.severity(Severity.CRITICAL)
@allure.title('Add, select, update, delete project')
def test_add_select_update_delete_project(testrail_session, delete_project_before, aunthatification):
    with allure.step('Add project'):
        response_add = testrail_session.post(url='/add_project',
                  headers={'Authorization': 'Basic ' + aunthatification, 'Content-Type': 'application/json'},
                  json={'name': 'Projet X'})
        id = response_add.json()['id']

    with allure.step('Select project'):
        response_select = testrail_session.get(url=f'/get_project/{id}',
                           headers={'Authorization': 'Basic ' + aunthatification})

    with allure.step('Uptate project'):
        response_update = testrail_session.post(url=f'/update_project/{id}',
                           headers={'Authorization': 'Basic ' + aunthatification},
                           json={'name': 'Projet New'})
    with allure.step('Delete project'):
        response_delete = testrail_session.post(url=f'/delete_project/{id}',
                          headers={'Authorization': 'Basic ' + aunthatification, 'Content-Type': 'application/json'})

    with allure.step('Result'):
        assert response_add.status_code == 200
        assert response_add.json()['id'] != None
        assert response_select.status_code == 200
        assert response_add.json()['id'] == response_select.json()['id']
        assert response_update.status_code == 200
        assert response_add.json()['id'] == response_update.json()['id']
        assert response_update.json()['name'] == 'Projet New'
        assert response_delete.status_code == 200


@allure.tag("api")
@allure.label('owner', 'Elena')
@allure.feature('API')
@allure.story('Add project')
@allure.severity(Severity.CRITICAL)
@allure.title('Add project positive case')
@pytest.mark.parametrize('name, announacement, show_announcement, suite_mode', [
                         pytest.param('l', '', '', '', id='project have name length 1 character'),
                         pytest.param('l'*120, '', '', '', id='project have name length 120 character'),
                         pytest.param('l'*250, '', '', '', id='project have name length 250 character'),
                         pytest.param('l', 'a', '', '', id='project have name and announcement'),
                         pytest.param('l', '', True, '', id='project have name, announcement, show_announcement=True'),
                         pytest.param('l', '', False, '', id='project have name, announcement, show_announcement=False'),
                         pytest.param('l', '', True, 1, id='project have name, announcement, show_announcement,suite_mode=1'),
                         pytest.param('l', '', True, 2, id='project have name, announcement, show_announcement, suite_mode=2'),
                         pytest.param('l', 'a', True, 3, id='project have name, announcement, show_announcement, suite_mode=3')]
                         )
def test_add_project_positive_case(
        testrail_session, delete_project_before, delete_project_later, aunthatification, name, announacement, show_announcement, suite_mode):
    with allure.step('Add project'):
        response = testrail_session.post(url='/add_project',
                           headers={'Authorization': 'Basic ' + aunthatification, 'Content-Type': 'application/json'},
                           json={'name': name, 'announcement': announacement, 'show_announcement': show_announcement, 'suite_mode': suite_mode
                          })

    with allure.step('Result'):
        assert response.status_code == 200
        assert response.json()['id'] != None
        assert response.json() == S(CreatePprojectSchema)


@allure.tag("api")
@allure.label('owner', 'Elena')
@allure.feature('API')
@allure.story('Add project')
@allure.severity(Severity.CRITICAL)
@allure.title('Add project negative case')
@pytest.mark.parametrize('name, announacement, show_announcement, suite_mode', [
                         pytest.param('', '', True, 1, id='project not have name'),
                         pytest.param('l'*251, 'a', True, 1, id='project have name len=251'),
                         pytest.param('l', '', True, 4, id='project have name, but suite_mode=4')])
def test_add_project_negative_case(testrail_session, aunthatification, name, announacement, show_announcement, suite_mode):
    with allure.step('Add project'):
        response = testrail_session.post(url='/add_project',
                             headers={'Authorization': 'Basic ' + aunthatification, 'Content-Type': 'application/json'},
                             json={'name': name, 'announcement': announacement,
                                   'show_announcement': show_announcement, 'suite_mode': suite_mode
                                   })
    with allure.step('Result'):
        assert response.status_code == 400


@allure.tag("api")
@allure.label('owner', 'Elena')
@allure.feature('API')
@allure.story('Update project')
@allure.severity(Severity.CRITICAL)
@allure.title('Update project negative case')
def test_update_project_negative_case(testrail_session, aunthatification):

    with allure.step('Update project'):
        response_update = testrail_session.post(url=f'/update_project/{1}',
                           headers={'Authorization': 'Basic ' + aunthatification},
                           json={'name': 'Projet New'})
    with allure.step('Result'):
        assert response_update.status_code == 200
        assert response_update.json() == {'error': 'Field :project_id is not a valid or accessible project.'}


@allure.tag("api")
@allure.label('owner', 'Elena')
@allure.feature('API')
@allure.story('Delete project')
@allure.severity(Severity.CRITICAL)
@allure.title('Delete project negative case')
def test_delete_project_negative_case(testrail_session, aunthatification):

    with allure.step('Delete progect'):
        response_delete = testrail_session.post(url=f'/delete_project/{1}',
                          headers={'Authorization': 'Basic ' + aunthatification(), 'Content-Type': 'application/json'})

    with allure.step('Result'):
        assert response_delete.status_code == 400
        assert response_delete.json() == {'error':'Field :project_id is not a valid or accessible project.'}
