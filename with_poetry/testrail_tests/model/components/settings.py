from selene.support.shared import browser


class Settings:
    @staticmethod
    def navigation():
        browser.element('a[id ="navigation-admin"]').click()

    @staticmethod
    def project():
        browser.element('a[id="navigation-sub-projects"]').click()

    @staticmethod
    def select_deleting():
        browser.element('[class ="odd hoverSensitive"]>:nth-child(3)>a>div').click()