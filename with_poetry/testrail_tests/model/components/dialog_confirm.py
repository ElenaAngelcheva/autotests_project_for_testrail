from selene.support.shared import browser
from selene import have


class DialogConfirm:
    @staticmethod
    def delete():
        browser.element('span[class="dialog-confirm"]>strong').click()

    @staticmethod
    def submit():
        browser.element('[id="deleteDialog"]>:nth-child(3)>a').click()

    @staticmethod
    def lack_project():
        browser.element('[class="grid"]>tbody>tr>td').should(have.exact_text('No projects.'))