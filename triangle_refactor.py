#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 10:55:55 2019

@author: jzuluaga
"""

#Import numpy 
import numpy as np

#Factors to convert from and to radians
convert_to_deg=180/np.pi
convert_to_rad=np.pi/180

class triangulo(object):
    """
    Triangle class including some generic methods.
    
    Being an almost abstract class no init method is defined.
    
    ChangesLog:
        v1. Jorge Zuluaga.  Test class.
        v2. Jorge Zuluaga.  Units corrected.
    """
    #Valores
    a=0;b=0;c=0
    A=0;B=0;C=0
    #Otras propiedades
    base=0
    altura=0
    
    """
    #Uncomment in case you need it
    def sinTheorem(self,a,b,B):
        return np.arcsin(a*np.sin(B)/b)
    """

    ########################################################
    #OBTAIN ANGLES
    ########################################################    
    def angleA(self):
        if self.A>0:pass
        elif self.B>0:
            self.A=np.arcsin(self.a*np.sin(self.B)/self.b)
        elif self.C>0:
            self.A=np.arcsin(self.a*np.sin(self.C)/self.c)

    def angleB(self):
        if self.B>0:pass
        elif self.A>0:
            self.B=np.arcsin(self.b*np.sin(self.A)/self.a)
        elif self.C>0:
            self.B=np.arcsin(self.b*np.sin(self.C)/self.c)
    
    def angleC(self):
        if self.C>0:pass
        elif self.A>0:
            self.C=np.arcsin(self.c*np.sin(self.A)/self.a)
        elif self.B>0:
            self.C=np.arcsin(self.c*np.sin(self.B)/self.b)

    def getAngles(self):
        self.angleA()
        self.angleB()
        self.angleC()
        return self.A*convert_to_deg,\
                self.B*convert_to_deg,\
                self.C*convert_to_deg

    #Area
    def getArea(self):
        return 0.5*self.h*self.bas

    def getPerimeter(self):
        return self.a+self.b+self.c

###########################################################
#SPECIFIC CLASSES
###########################################################
class RightTriangle(triangulo):
    """
    Triangulo rectangulo
    """
    def __init__(self,a,b):
        self.a=a
        self.b=b
        #This is the Pitagoras' theorem
        self.c=np.sqrt(a**2+b**2)
        self.bas=a
        self.h=b
        #Convert degrees to radians
        self.C=90*convert_to_rad
        
    def AreaRightTriangle(self):
        return self.getArea()

class IsocelesTriangle(triangulo):
    """
    Triangulo isoceles
    """
    def __init__(self,a,b):
        #Lado a
        self.a=a
        #Lado b
        self.b=b
        #Lado c
        self.c=a
        #Angulo A
        self.A=np.arccos((b/2)/a)
        #Base
        self.bas=b
        #Altura
        self.h=a*np.sin(self.A)

    def AreaIsocelesTriangle(self):
        base_triangulo=self.b
        altura_triangulo=self.a*np.sin(self.A)
        area_del_triangulo_isoceles=(1.0/2.0)*base_triangulo*altura_triangulo
        return area_del_triangulo_isoceles
