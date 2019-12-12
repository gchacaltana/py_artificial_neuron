# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Artificial Neuron
__author__ = "Gonzalo Chacaltana Buleje"
__email__ = "gchacaltanab@gmail.com"


class ArtificialNeuron(object):
    def __init__(self, x, w, u, u_w, transfer_code):
        self.x = x
        self.w = w
        self.u = u
        self.u_w = u_w
        self.transfer_code = transfer_code
        self.r = 0

    def execute(self):
        self.execute_sum_xw()
        self.execute_activation()

    def execute_sum_xw(self):
        ni = 0
        for i in range(len(self.x)):
            ni += self.x[i]*self.w[i]
        ni += self.u*self.u_w
        ni = round(ni, 2)
        print("ni : ", ni)

    def execute_activation(self):

    def activation_sigmoidal(self):
        pass

    def activation_escalon_unitario(self):
        pass

    def getResult(self):
        return self.r
