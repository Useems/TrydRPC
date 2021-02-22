import time
from utils.process import enum_processes, enum_process_windows
from pypresence import Presence

class Client:
    def __init__(self):
        self.tryd = {"version": None, "plataform": None, "account": None, "isReplay": None, "isSimulator": None, "isLoading": True}
        
        self.detectionAttempt = 0
        self.lastConnection = None
        self.lastStatus = None
        
        self.presence = Presence("800798245570740294")
        self.connect()
        
        print("Client has connected!")

        self.loop()

    def connect(self):
        while True:
            try:
                self.presence.connect()
                break
            except Exception as err:
                print(err)
                time.sleep(10)

    def loop(self):
        while True:
            status = False
            self.detectionAttempt += 1

            for pid, name in enum_processes(process_name="javaw.exe"):
                data = enum_process_windows(pid)

                for _, title in data:
                    if title.startswith("Tryd "):
                        status = True
                        info = title.split(" - ")

                        self.tryd = {
                            "version": info[0].split(' ')[1],
                            "plataform": info[1],
                            "account": info[len(info) - 1],
                            "isReplay": "REPLAY" in info,
                            "isSimulator": "TrydSIM" in info,
                            "isLoading": False
                        }
                    elif title.startswith("Trader"):
                        status = True

            if status:
                self.detectionAttempt = 0

            if not status and ("version" in self.tryd and self.lastConnection != None and self.detectionAttempt < 5):
                status = True

            if self.detectionAttempt > 0:
                self.tryd["isLoading"] = True
                self.tryd["isReplay"] = False
                self.tryd["isSimulator"] = False

            if status and not self.lastStatus:
                self.lastConnection = time.time()

            if status and self.lastStatus:
                self.presence.update(
                    details=self.tryd["isReplay"] and "Em replay" or self.tryd["isSimulator"] and "Em simulador" or "Carregando...",
                    start=self.lastConnection,
                    large_image="logo",
                    large_text="Tryd {0} {1}".format(self.tryd["plataform"], self.tryd["version"]),
                    small_image=(self.tryd["isLoading"] or (not self.tryd["isReplay"] and not self.tryd["isSimulator"])) and "yellow" or self.tryd["isReplay"] and "replay" or "green",
                    small_text=self.tryd["isReplay"] and "Replay de Mercado" or self.tryd["isSimulator"] and "Simulador de Mercado" or self.tryd["isLoading"] and "Coletando informações" or None
                )
            
            if not status and self.lastStatus:
                self.presence.clear()

            self.lastStatus = status
            
            time.sleep(1)