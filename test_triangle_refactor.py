#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
import triangle_refactor as tri
import numpy as np

class TestTriangles(unittest.TestCase):

    def test_hipotenusa(self):
        r=tri.RightTriangle(3,4)
        self.assertEqual(r.c,5)

    def test_equilatero(self):
        e=tri.IsocelesTriangle(2,2)
        self.assertAlmostEqual(e.A*180/np.pi,60.0,7)
        
    def test_isoceles(self):
        i=tri.IsocelesTriangle(5,8)
        self.assertAlmostEqual(i.h,3.0,7)

    def test_angles(self):
        t=tri.triangulo()
        t.a=1
        t.b=1
        t.c=np.sqrt(2)
        t.A=45.0*np.pi/180
        A,B,C=t.getAngles()
        self.assertAlmostEqual(A,45,7)
        self.assertAlmostEqual(B,45,7)
        self.assertAlmostEqual(C,90,7)
    
    def test_area_isoceles(self):
        i=tri.IsocelesTriangle(5,8)
        self.assertAlmostEqual(i.AreaIsocelesTriangle(),12.0,7)
            
    def test_area_right(self):
        r=tri.RightTriangle(3,4)
        self.assertAlmostEqual(r.AreaRightTriangle(),6.0,7)

    def test_perimeter(self):
        t=tri.triangulo()
        t.a=1
        t.b=1
        t.c=1
        self.assertAlmostEqual(t.getPerimeter(),3.0,7)
