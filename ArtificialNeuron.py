# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Artificial Neuron - Apply Forward Propagation
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
        self.activation()

    def execute_sum_xw(self):
        self.ni = 0
        for i in range(len(self.x)):
            self.ni += self.x[i]*self.w[i]
        self.ni += self.u*self.u_w
        self.ni = round(self.ni, self.round)
        print("ni : ", self.ni)

    def activation(self):
        """Función de activación"""
        self.sigmoidal_activation()
        self.unit_step_activation()

    def sigmoidal_activation(self):
        """Función de activación sigmoidal"""
        if self.transfer_code == 1:
            self.y = round(1/(1+math.pow(math.e, self.ni*-1)), self.round)

    def unit_step_activation(self):
        """Función de activación de escalón unitario"""
        if self.transfer_code == 2:
            self.y = round(1 if self.ni > 0 else 0, self.round)

    def showResult(self):
        print("yi = f(x,w): %s" % self.y)
    
    def showNi(self):
        print("ni : ", self.ni)