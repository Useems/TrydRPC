import os, sys
import pymsgbox
from PIL import Image
from pystray import Icon as icon, Menu as menu, MenuItem as item
from threading import Thread

class Stray:
    def __init__(self, version=''):
        self.title = 'TrydRPC'
        self.version = version

        self.image = Image.open(os.path.join(sys._MEIPASS if hasattr(sys, '_MEIPASS') else '', 'assets', 'app.ico'))

        self.menu = menu(
            item(self.title + ' v' + self.version, None, enabled=False),
            menu.SEPARATOR,
            item('Sobre', lambda: self.show_message_box('TrydRPC é um programa com o objetivo de mostrar as atividades da sua plataforma Tryd no Discord.')),
            item('Ajuda', lambda: self.show_message_box('Para que apareça em seu Discord as informações sobre a sua plataforma, é necessário que você vá até as suas configurações e ative a atividade de jogo, além de estar com o Tryd aberto. Se mesmo assim não funcionar, reinicie seu Discord e o TrydRPC.')),
            menu.SEPARATOR,
            item('Fechar', self.exit)
        )

        self.icon = icon(self.title, self.image, self.title, menu=self.menu)
        self.icon.run(self.init)

    def init(self, icon):
        icon.visible = True 

        print('Stray is running.')
        icon.notify('Em execução.', title='TrydRPC')

    def show_message_box(self, message=''):
        thread = Thread(target=pymsgbox.alert,args=[message, self.title + ' - v' + self.version, 'OK'])
        thread.start()

    def exit(self, icon):
        icon.visible = False
        icon.stop()
        os._exit(1)