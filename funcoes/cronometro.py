from datetime import date
import time


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
        ok = False
        while ok == False:
            valor = input('Quer iniciar o cronometro: ')
            valor = str(valor)
            ok = valor.capitalize()
            if ok == 'Sim':
                relogio = Cronometro()
                relogio.time_sec()
            else:
                ok = False


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
