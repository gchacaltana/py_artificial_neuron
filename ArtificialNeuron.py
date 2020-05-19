# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Artificial Neuron
__author__ = "Gonzalo Chacaltana Buleje"
__email__ = "gchacaltanab@gmail.com"

import sys
import math


class ArtificialNeuron(object):
    def __init__(self, x, w, u, u_w, transfer_code):
        self.x, self.w, self.u = x, w, u
        self.u_w, self.transfer_code = u_w, transfer_code
        self.ni, self.y = 0, 0

    def execute(self):
        self.execute_sum_xw()
        self.activation()

    def execute_sum_xw(self):
        self.ni = 0
        for i in range(len(self.x)):
            self.ni += self.x[i]*self.w[i]
        self.ni += self.u*self.u_w
        self.ni = round(self.ni, 2)
        self.showNi()

    def activation(self):
        """Función de activación"""
        self.sigmoidal_activation()
        self.unit_step_activation()

    def sigmoidal_activation(self):
        """Función de activación sigmoidal"""
        if self.transfer_code == 1:
            self.y = round(1/(1+math.pow(math.e, self.ni*-1)), 2)

    def unit_step_activation(self):
        """Función de activación de escalón unitario"""
        if self.transfer_code == 2:
            self.y = round(1 if self.ni > 0 else 0, 2)

    def showResult(self):
        print("yi = f(x,w): %s" % self.y)
    
    def showNi(self):
        print("ni : ", self.ni)