from threading import Thread
from modules import Stray, Client
from config import version

thread = Thread(target=Stray,args=[version])

thread.start()
Client()
thread.join()