from selene.support.shared import browser


class Authorization:
    def open_authorization_pege(self, value):
        browser.open(value)
        return self

    def set_login_email(self, value):
        browser.element('input[id="name"]').type(value)
        return self

    def set_password(self, value):
        browser.element('input[id="password"]').type(value)
        return self

    @staticmethod
    def submit():
        browser.element('button[id="button_primary"]').click()