from selene.support.shared import browser
from selene import have


class Authorization:
    def open_authorization_page(self, value):
        browser.open(value)
        return self

    def set_login_email(self, value):
        browser.element('input[id="name"]').type(value)
        return self

    def set_password(self, value):
        browser.element('input[id="password"]').type(value)
        return self

    @staticmethod
    def submit_auht():
        browser.element('button[id="button_primary"]').click()

    @staticmethod
    def checking_title():
        browser.element('div[class ="top-section text-ppp"]').should(have.exact_text('TestRail QA'))

    @staticmethod
    def checking_loginpage_message_title():
        browser.element('div[class="error-text"]').should(have.exact_text(
            'Email/Login or Password is incorrect. Please try again.'))
