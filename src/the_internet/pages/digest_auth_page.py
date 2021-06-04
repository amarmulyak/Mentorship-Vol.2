from src.the_internet.pages.basic_auth_page import BasicAuthPage


# TODO Чи ок наслідувати чи краще виносити в комон обджекти
class DigestAuthPage(BasicAuthPage):

    def get_digest_auth_page(self, username, password):
        return self._get_auth_page(username, password, last_segment="digest_auth")
