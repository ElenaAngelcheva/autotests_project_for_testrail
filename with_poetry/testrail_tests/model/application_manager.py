from with_poetry.testrail_tests.model.components.authorization import Authorization
from with_poetry.testrail_tests.model.components.dialog_confirm import DialogConfirm
from with_poetry.testrail_tests.model.components.new_project import AddProject
from with_poetry.testrail_tests.model.components.settings import Settings


class Application_manager:
    auth = Authorization()
    add = AddProject()
    settings = Settings()
    confirm = DialogConfirm()




app = Application_manager