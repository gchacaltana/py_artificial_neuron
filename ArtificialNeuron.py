# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Artificial Neuron
__author__ = "Gonzalo Chacaltana Buleje"
__email__ = "gchacaltanab@gmail.com"

import sys
import math


class ArtificialNeuron(object):
    def __init__(self, x, w, u, u_w, transfer_code):
<<<<<<< HEAD
        self.x = x
        self.w = w
        self.u = u
        self.u_w = u_w
        self.transfer_code = transfer_code
        self.ni = 0
        self.y = 0
        self.round = 4
=======
        self.x, self.w, self.u = x, w, u
        self.u_w, self.transfer_code = u_w, transfer_code
        self.ni, self.y = 0, 0
>>>>>>> c8d1d818fefeb265754bf7d1f9c4d8a9954d0fd8

    def execute(self):
        self.execute_sum_xw()
        self.activation()

    def execute_sum_xw(self):
        self.ni = 0
        for i in range(len(self.x)):
            self.ni += self.x[i]*self.w[i]
        self.ni += self.u*self.u_w
<<<<<<< HEAD
        self.ni = round(self.ni, self.round)
        print("ni : ", self.ni)
=======
        self.ni = round(self.ni, 2)
        self.showNi()
>>>>>>> c8d1d818fefeb265754bf7d1f9c4d8a9954d0fd8

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