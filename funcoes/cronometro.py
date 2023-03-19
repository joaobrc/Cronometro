from datetime import date, datetime,timedelta
#import PySimpleGUI as sg
import time
import os

class windo:
    def __init__(self):
        pass

    @staticmethod
    def janela():
        sg.theme('BlueMono')
        
        layout = [[sg.Text("Cronometro")],
                [sg.Text('Click no botao')],
                [sg.Button("ok", enable_events=True)]]
        windonw = sg.Window('Cronometro', layout)

        while True:
            event, valor = windonw.read()
            if event == 'ok' or event == sg.WIN_CLOSED:
                break
    
        windonw.close()
        return event

class Data:
    def __init__(self):
        pass

    def __str__(self):
        return self.data_hoje()

    @staticmethod
    def data_hoje():
        hoje = date.today()
        hoje_covertido = hoje.strftime("%d/%m/%Y")
        dia = "Hoje é {}".format(hoje_covertido)
        return dia

class Inciar:

    @staticmethod
    def comecar():
        valor = windo.janela()
        valor = str(valor)
        if valor == 'ok':
            relogio = Cronometro()
            relogio.time_sec()

class Cronometro:

    def __init__(self):
        self.tempo = 0

    def time_sec(self):
        while self.tempo < 1000:
            m, s = divmod(self.tempo, 60)
            numero_sec = '{:02d}:{:02d}'.format(m, s)
            self.tempo += 1
            time.sleep(1)
            print(numero_sec)
        print("00:00")


class Fecha_Musica:
    def __init__(self,time,parametro) -> None:
        
        self.fecha = Fecha_Musica.paramentros(time=time)[parametro]
        
    @classmethod
    def paramentros(cls,time):
        parametro={
            "hora":(datetime.now() + timedelta(hours=time)).isoformat(timespec="minutes"),
            "minutos":(datetime.now() + timedelta(minutes=time)).isoformat(timespec="minutes"),
        }
        return parametro
    

    def contador(self):
        agr = False
        while not agr:
            self.agora = datetime.now().isoformat(timespec='minutes')
            if self.fecha == self.agora:
                os.system("taskkill /im chrome.exe /f")
                agr = True
