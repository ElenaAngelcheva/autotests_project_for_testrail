from selene.support.shared import browser
from selene import have


class DialogConfirm:
    @staticmethod
    def dialog_confirm():
        browser.element('span[class="dialog-confirm"]>strong').click()

    @staticmethod
    def submit_delete_dialog():
        browser.element('[id="deleteDialog"]>:nth-child(3)>a').click()

    @staticmethod
    def cheacking_lack_project():
        browser.element('[class="grid"]>tbody>tr>td').should(have.exact_text('No projects.'))