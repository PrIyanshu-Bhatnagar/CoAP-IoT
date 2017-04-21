import sys
from Client import client1, client2
from Server import server

class AppUI():

    c1 = False
    c2 = False

    def client_1_buttonClicked(self):
        if self.c1 is False:
            client1.client_1_connect()
        else:
            client1.client_1_stop()

    def client_1_get_buttonClicked(self):
        client1.client_1_get()

    def client_1_put_buttonClicked(self):
        client1.client_1_put("")

    def client_1_post_buttonClicked(self):
        client1.client_1_post("")

    def client_1_delete_buttonClicked(self):
        client1.client_1_delete()


    def client_2_buttonClicked(self):
        if self.c2 is False:
            client2.client_2_connect()
        else:
            client2.client_2_stop()

    def client_2_get_buttonClicked(self):
        client2.client_2_get()

    def client_2_put_buttonClicked(self):
        client2.client_2_put("")

    def client_2_post_buttonClicked(self):
        client2.client_2_post("")

    def client_2_delete_buttonClicked(self):
        client2.client_2_delete()


    def server_buttonClicked(self):
        server.get_server()

    def update_Information(self):
        pass


def main():
    app = QApplication(sys.argv)
    form = AppUI()
    form.show()


    app.exec_()


if __name__ == '__main__':
    x = AppUI()
    x.server_buttonClicked()
    x.client_1_buttonClicked()
    x.client_2_buttonClicked()
