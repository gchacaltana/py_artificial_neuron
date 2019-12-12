# !/usr/bin/env python
# -*- coding: utf-8 -*-
# App
__author__ = "Gonzalo Chacaltana Buleje"
__email__ = "gchacaltanab@gmail.com"

from ArtificialNeuron import ArtificialNeuron


class App(object):
    def __init__(self):
        self.entries = 0
        self.x = []  # valores de entrada
        self.w = []  # pesos de las entradas
        self.u = 1  # umbral
        self.u_w = 0.5  # peso de umbral
        self.transfer_code = 0  # codigo de función de transferencia

    def insert_values(self):
        self.insert_x()
        self.insert_w()
        self.insert_umbral()
        self.insert_activation()

    def insert_x(self):
        self.entries = int(
            input("Ingrese cantidad de entradas (x) de la neurona artificial: "))
        c = 0
        while len(self.x) < self.entries:
            c += 1
            self.x.append(float(input("Ingrese el valor de X%s: " % c)))

    def insert_w(self):
        if (int(self.entries) > 0):
            c = 0
            while len(self.w) < self.entries:
                c += 1
                self.w.append(float(input("Ingrese el valor de W%s: " % c)))

    def insert_umbral(self):
        if (int(self.entries) > 0):
            self.u = float(input("Ingrese el valor del umbral: "))
            self.u_w = float(input("Ingrese el peso del umbral: "))

    def insert_activation(self):
        print("Funcion de Transferencia")
        print("[1] Sigmoidal")
        print("[2] Escalon Unitario")
        while int(self.transfer_code) <= 0:
            self.transfer_code = int(input("Ingrese una opcion: "))

    def show_result(self):
        if (len(self.x) > 0 and len(self.w) > 0 and self.u > 0 and self.transfer_code > 0):
            an = ArtificialNeuron(self.x, self.w, self.u,
                                  self.u_w, self.transfer_code)
            an.execute()
            print("Resultado: %s" % an.getResult())


if __name__ == "__main__":
    application = App()
    application.insert_values()
    application.show_result()
