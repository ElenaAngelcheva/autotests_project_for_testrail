from selene.support.shared import browser
from selene import have


class AddProject:
    @staticmethod
    def new_project():
        browser.element('a[id = "sidebar-projects-add"]').click()

    def neme_project(self, value):
        browser.element('input[id = "name"]').type(value)
        return self

    def announcement_project(self, value):
        browser.element('[id = "announcement"]').type(value)
        return self

    @staticmethod
    def show_announcement():
        browser.element('[id = "show_announcement"]').click()

    @staticmethod
    def suites_model_multiple ():
        browser.element('[id = "suite_mode_multi"]').click()

    @staticmethod
    def confirm():
        browser.element('[id = "accept"]').click()

    def create_check(self, value):
        browser.element('a[id="navigation-project"]').should(have.exact_text(value))

