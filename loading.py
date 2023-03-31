import time 
from time import sleep 
import os 
from os import * 

def Limpar_tela():
    system("cls")

def loading():
    Limpar_tela()
    print("Loading[=         ]%10")
    sleep(0.2)
    Limpar_tela()
    print("Loading[==        ]%20")
    sleep(0.2)
    Limpar_tela()
    print("Loading[===       ]%30")
    sleep(0.2)
    Limpar_tela()
    print("Loading[====      ]%40")
    sleep(0.2)
    Limpar_tela()
    print("Loading[=====     ]%50")
    sleep(0.2)
    Limpar_tela()
    print("Loading[======    ]60%")
    sleep(0.2)
    Limpar_tela()
    print("Loading[=======   ]%70")
    sleep(0.2)
    Limpar_tela()
    print("Loading[========  ]%80")
    sleep(0.2)
    Limpar_tela()
    print("Loading[========= ]%90")
    sleep(0.2)
    Limpar_tela()
    print("Loading[==========]100%")
    sleep(0.2)
    Limpar_tela()
    print("----Sucessfull----")
    sleep(2)
    Limpar_tela()
loading()