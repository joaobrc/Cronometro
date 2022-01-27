from datetime import date


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


class Cronometro:

    def __init__(self, tempo):
        self.tempo = tempo

    def time_sec(self):
        while self.tempo > 0:
            m, s = divmod(self.tempo, 60)
            numero_sec = '{:02d}:{:02d}'.format(m, s)
            self.tempo -= 1
            print(numero_sec)
        print("00:00")
