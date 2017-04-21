import sys
from 

class AppUI():

    def client_1_buttonClicked(self):
        pass

    def client_2_buttonClicked(self):
        pass

    def server_buttonClicked(self):
        pass

    def update_Information(self):
        pass


def main():
    app = QApplication(sys.argv)
    form = AppUI()
    form.show()

    app.exec_()


if __name__ == '__main__':
    main()