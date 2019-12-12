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
        pass

    def getResult(self):
        return self.r
