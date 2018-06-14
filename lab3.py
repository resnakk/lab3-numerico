# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""
#=============================================================#
#========================= Constructor =======================#
#=============================================================#
import numpy as np
Matrices = []
#------------------------------MATRIZ A---------------------
matrizA = np.zeros((100,100))
for i in range(100):
    for j in range(100):
        dif = i - j
        if i == j:
            matrizA[i,j] = 2
        elif i < j and dif == -1:
            matrizA[i,j] = 7
        elif i > j and dif == 1:
            matrizA[i,j] = 5
Matrices.append(matrizA)
#------------------------------MATRIZ B---------------------
matrizB = np.zeros((100,100))
for i in range(100):
    for j in range(100):
        
        if i == j:
            matrizB[i,j] = 3
        elif i > j:
            matrizB[i,j] = 9
Matrices.append(matrizB)
#------------------------------MATRIZ C---------------------            
matrizC = np.zeros((100,100))            
for i in range( 1, 101):
    for j in range(1, 101):
        matrizC[i - 1,j -1] = max(i, j)
Matrices.append(matrizC)
#------------------------------MATRIZ D---------------------            
matrizD = np.ones((100,100))
for i in range(1,101):
    for j in range(1,1001):
            if i == 2*j:
                matrizD[i-1,j-1] = i**2 + j**2
Matrices.append(matrizD)

#=============================================================#
#============================== P1 ===========================#
#=============================================================#
for i in Matrices:
    p = 0
    n = 0
    Valores, Vectores = np.linalg.eig(i)
    for v in Valores:
        if v > 0:
            p += 1
        elif v <= 1:
            n += 1 
    if p > 0 and n == 0:
        print i, "\n","Semi definida positiva."
    elif n > 0 and p == 0:
        print i, "\n","Semi definida negativa."
    else: 
        print i, "\n","No es nada."
#=============================================================#
#============================== P2 ===========================#
#=============================================================#          
print "Cabe destacar que para abrir la foto lab3.py debe estar en la misma carpeta que la foto a evaluar"
from PIL import Image
def AbrirImagen(Imagen):
    Ruta = ( Imagen)
    nombre = Imagen.split('.')
    Imagen = Image.open(Ruta)
    Imagen.show()
    CopiaImagen = Imagen
    for i in range(CopiaImagen.size[0]):
        for j in range(CopiaImagen.size[1]):
            if i == j:
                Pixel = tuple([0,0,0])
                CopiaImagen.putpixel((i, j), Pixel)  
    
    CopiaImagen.show()                                                                                                                                                                                                                                                                                                                                                                                                                                                           
    CopiaImagen.save( nombre[0] + "2.png" )
    
    CopiaImagen2 = Imagen
    for i in range(CopiaImagen2.size[0] - 1):
        for j in range(CopiaImagen2.size[1] - 1):
            if i == j:
                #=============================Columna 0 ================================================
                if i == 0 and j == 0:
                    r12, g12, b12 = CopiaImagen2.getpixel((i, j + 1))
                    r21, g21, b21 = CopiaImagen2.getpixel((i + 1, j))
                    rp, gp, bp = (r12 + r21)/2,(g12 + g21)/2,(b12 + b21)/2
                    prom = int( (rp + gp + bp) / 3 )
                    pixel = tuple([prom, prom, prom])
                    CopiaImagen2.putpixel((i,j), pixel)
                
                elif i < CopiaImagen2.size[0] and j == 0:
                    r11, g11, b11 = CopiaImagen2.getpixel((i - 1, j))
                    r22, g22, b22 = CopiaImagen2.getpixel((i, j + 1))
                    r31, g31, b31 = CopiaImagen2.getpixel((i + 1, j))
                    rp, gp, bp = (r11 + r22 + r31)/3,(g11 + g22 + g31)/3,(b11 + b22 + b31)/3  
                    pixel = tuple([rp, gp, bp])
                    CopiaImagen2.putpixel((i,j), pixel)
                
                elif i < CopiaImagen2.size[1] and j == 0  :
                    r21, g21, b21 = CopiaImagen2.getpixel((i - 1, j))
                    r22, g22, b22 = CopiaImagen2.getpixel((i,j + 1))
                    rp, gp, bp = (r22 + r21)/2,(g22 + g21)/2,(b22 + b21)/2   
                    prom = int( (rp + gp + bp) / 3 )
                    pixel = tuple([prom, prom, prom])
                    CopiaImagen2.putpixel((i,j), pixel)
                #=============================Columna n ================================================
                elif i == 0 and j == CopiaImagen2.size[1]:
                    r12, g12, b12 = CopiaImagen2.getpixel((i, j - 1))
                    r21, g21, b21 = CopiaImagen2.getpixel((i + 1, j))
                    rp, gp, bp = (r12 + r21)/2,(g12 + g21)/2,(b12 + b21)/2  
                    prom = int( (rp + gp + bp) / 3 )
                    pixel = tuple([prom, prom, prom])
                    CopiaImagen2.putpixel((i,j), pixel)
                
                elif i < CopiaImagen2.size[0]  and j == CopiaImagen2.size[1]:
                    r11, g11, b11 = CopiaImagen2.getpixel((i + 1, j))
                    r22, g22, b22 = CopiaImagen2.getpixel((i, j - 1))
                    r31, g31, b31 = CopiaImagen2.getpixel((i + 1,j))
                    rp, gp, bp = (r11 + r22 + r31)/3,(g11 + g22 + g31)/3,(b11 + b22 + b31)/3  
                    prom = int( (rp + gp + bp) / 3 )
                    pixel = tuple([prom, prom, prom])
                    CopiaImagen2.putpixel((i,j), pixel)
                
                elif i == CopiaImagen2.size[0] and j == CopiaImagen2.size[1]:
                    r21, g21, b21 = CopiaImagen2.getpixel((i - 1,j))
                    r22, g22, b22 = CopiaImagen2.getpixel((i,j - 1))
                    rp, gp, bp = (r22 + r21)/2,(g22 + g21)/2,(b22 + b21)/2   
                    prom = int( (rp + gp + bp) / 3 )
                    pixel = tuple([prom, prom, prom])
                    CopiaImagen2.putpixel((i,j), pixel)
                #============================= Fila 0 y Fila n ================================================                               
                elif i == 0  and j < CopiaImagen2.size[1]:
                    r11, g11, b11 = CopiaImagen2.getpixel((i, j - 1))
                    r22, g22, b22 = CopiaImagen2.getpixel((i + 1, j))
                    r31, g31, b31 = CopiaImagen2.getpixel((i,j + 1))
                    rp, gp, bp = (r11 + r22 + r31)/3,(g11 + g22 + g31)/3,(b11 + b22 + b31)/3  
                    prom = int( (rp + gp + bp) / 3 )
                    pixel = tuple([prom, prom, prom])
                    CopiaImagen2.putpixel((i,j), pixel)
                
                elif i == CopiaImagen2.size[1]  and j < CopiaImagen2.size[1]:
                    r11, g11, b11 = CopiaImagen2.getpixel((i, j - 1))
                    r22, g22, b22 = CopiaImagen2.getpixel((i - 1, j))
                    r31, g31, b31 = CopiaImagen2.getpixel((i,j + 1))
                    rp, gp, bp = (r11 + r22 + r31)/3,(g11 + g22 + g31)/3,(b11 + b22 + b31)/3  
                    prom = int( (rp + gp + bp) / 3 )
                    pixel = tuple([prom, prom, prom])
                    CopiaImagen2.putpixel((i,j), pixel)
                    
                #============================= Fila x columna y ================================================
                elif i < CopiaImagen2.size[0] and j < CopiaImagen2.size[1]:
                    r21, g21, b21 = CopiaImagen2.getpixel((i, j - 1))
                    r12, g12, b12 = CopiaImagen2.getpixel((i - 1, j))
                    r32, g32, b32 = CopiaImagen2.getpixel((i + 1,j))
                    r23, g23, b23 = CopiaImagen2.getpixel((i, j + 1))
                    rp, gp, bp = (r21 + r12 + r32 + r23)/4,(g21 + g12 + g32 + g23)/4,(b21 + b12 + b32 + b23)/4 
                    prom = int( (rp + gp + bp) / 3 )
                    pixel = tuple([prom, prom, prom])
                    CopiaImagen2.putpixel((i,j), pixel)

    CopiaImagen2.show()                                                                                                                                                                                                                                                                                                                                                                                                                                                           
    CopiaImagen2.save(nombre[0] + "3.png")
#Corriendo el programa
AbrirImagen("foto.jpg")

            
                
            
            
            
            
            
            
            
            
