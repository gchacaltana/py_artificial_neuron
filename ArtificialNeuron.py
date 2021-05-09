# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Artificial Neuron
__author__ = "Gonzalo Chacaltana Buleje"
__email__ = "gchacaltanab@gmail.com"

import sys
import math


class ArtificialNeuron(object):
    def __init__(self, x, w, u, u_w, transfer_code):
        self.x = x
        self.w = w
        self.u = u
        self.u_w = u_w
        self.transfer_code = transfer_code
        self.ni = 0
        self.y = 0
        self.round = 4

    def execute(self):
        self.execute_sum_xw()
        self.execute_activation()

    def execute_sum_xw(self):
        self.ni = 0
        for i in range(len(self.x)):
            self.ni += self.x[i]*self.w[i]
        self.ni += self.u*self.u_w
        self.ni = round(self.ni, self.round)
        print("ni : ", self.ni)

    def execute_activation(self):
        self.activation_sigmoidal()
        self.activation_escalon_unitario()

    def activation_sigmoidal(self):
        if self.transfer_code == 1:
            self.y = round(1/(1+math.pow(math.e, self.ni*-1)), self.round)

    def activation_escalon_unitario(self):
        if self.transfer_code == 2:
            self.y = round(1 if self.ni > 0 else 0, self.round)

    def showResult(self):
        print("yi = f(x,w): %s" % self.y)