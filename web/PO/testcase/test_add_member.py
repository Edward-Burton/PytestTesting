from web.PO.page.main import Main


class Test_Addmember():
    def setup(self):
        self.main = Main()

    def test_add_member(self):
        assert  self.main.goto_add_member().add_member().get_top_contact(property="name") == "丁海寅"