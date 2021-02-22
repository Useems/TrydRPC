from threading import Thread
from modules import Stray, Client

thread = Thread(target=Stray)

thread.start()
Client()
thread.join()