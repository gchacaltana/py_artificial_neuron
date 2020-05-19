# !/usr/bin/env python
# -*- coding: utf-8 -*-
# App
__author__ = "Gonzalo Chacaltana Buleje"
__email__ = "gchacaltanab@gmail.com"

from ArtificialNeuron import ArtificialNeuron


class App(object):
    def __init__(self):
        """
        x = valores de entrada
        w = pesos de entrada
        u = umbral
        u_w = peso de umbral
        activation_code = Código de Función de Transferencia (Activación)
        """
        self.entries = 0
        self.x, self.w = [], []
        self.u, self.u_w = 1, 0.5
        self.activation_code = 0

    def input_values(self):
        self.input_entries()
        self.input_x()
        self.input_w()
        self.input_umbral()
        self.input_activation()

    def input_entries(self):
        self.entries = int(
            input("Ingrese cantidad de entradas para la neurona artificial: "))

    def input_x(self):
        counter = 0
        while len(self.x) < self.entries:
            counter += 1
            self.x.append(
                float(input("Ingrese el valor de x[{}]: ".format(counter))))

    def input_w(self):
        if (int(self.entries) > 0):
            counter = 0
            while len(self.w) < self.entries:
                counter += 1
                self.w.append(
                    float(input("Ingrese el valor de w[{}]: ".format(counter))))

    def input_umbral(self):
        if (int(self.entries) > 0):
            self.u = float(input("Ingrese el valor del umbral: "))
            self.u_w = float(input("Ingrese el peso del umbral: "))

    def input_activation(self):
        print("Seleccione la función de activación")
        print("[1] Sigmoidal")
        print("[2] Escalon Unitario")
        while int(self.activation_code) <= 0:
            self.activation_code = int(input("Ingrese una opción: "))

    def show_result(self):
        if (len(self.x) > 0 and len(self.w) > 0 and self.u > 0 and self.activation_code > 0):
            an = ArtificialNeuron(self.x, self.w, self.u,
                                  self.u_w, self.activation_code)
            an.execute()
            an.showResult()


if __name__ == "__main__":
    try:
        application = App()
        application.input_values()
        application.show_result()
    except (ValueError, AttributeError, Exception) as ex:
        print(ex)
