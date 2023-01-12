from selene.support.shared import browser
from selene import have


class AddProject:
    @staticmethod
    def add_new_project():
        browser.element('a[id = "sidebar-projects-add"]').click()

    def set_name_project(self, value):
        browser.element('input[id = "name"]').type(value)
        return self

    def add_announcement_project(self, value):
        browser.element('[id = "announcement"]').type(value)
        return self

    @staticmethod
    def choice_show_announcement():
        browser.element('[id = "show_announcement"]').click()

    @staticmethod
    def choice_suites_model_multiple():
        browser.element('[id = "suite_mode_multi"]').click()

    @staticmethod
    def confirming_create_project():
        browser.element('[id = "accept"]').click()

    def checking_project_creation(self, value):
        browser.element('a[id="navigation-project"]').should(have.exact_text(value))

