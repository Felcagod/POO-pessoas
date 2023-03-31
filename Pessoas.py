import os 
from os import * 
import time 
from time import sleep 
import loading 
from loading import Limpar_tela
from loading import loading


class Pessoa():
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome 
        self.idade = idade 
        self.peso = peso 
        self.altura = altura 

    def envelhecer(self, anos):
        self.idade += anos 
        if self.idade < 21:
            self.crescer(anos*0.05)
    
    def crescer(self, cm):
        self.altura += cm 
    
    def engordar(self,kg):
        self.peso += kg 
    
    def emagrecer(self, kg):
        self.peso -= kg 
    
    def mudar_nome(self, novo_nome):
        self.nome = novo_nome 

def criar_pessoa():
    Limpar_tela() 
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    peso = float(input("Peso: "))
    altura = float(input("Altura: "))
    Limpar_tela()

    pessoa = Pessoa(nome, idade, peso, altura)

    while True: 
        
        print("\nOque voce quer fazer?")
        print("1. Ganhar peso")
        print("2. Perder peso")
        print("3. Ficar mais velho")
        print("4. Ficar mais alto")
        print("5. Mudar de nome")
        print("0. Sair")
        print()
        opcao = int(input("Digite a sua opcao: "))

        if opcao == 1:
            Limpar_tela()
            kg_ganhos = float(input("Quantos quilos voce quer ganhar?\n: "))
            pessoa.engordar(kg_ganhos)
            print(f"Novo peso: {pessoa.peso}")
        
        elif opcao == 2:
            Limpar_tela()
            kb_perdidos = float(input("Quantos quilos voce quer perder?\n: "))
            pessoa.emagrecer(kb_perdidos)
            print(f"Novo peso: {pessoa.peso}")
        
        elif opcao == 3:
            Limpar_tela()
            anos_envelhecimentos = int(input("Quantos anos voce quer envelhecer?\n: "))
            pessoa.envelhecer(anos_envelhecimentos)
            print(f"Nova idade: {pessoa.idade}")
            print(f"Nova altura: {pessoa.altura}")

        elif opcao == 4:
            Limpar_tela()
            cm_crecidos = float(input("Quantos centimetros voce quer crescer?\n: "))
            pessoa.crescer(cm_crecidos)
            print(f"Nova altura: {pessoa.altura}")
        
        elif opcao == 5:
            Limpar_tela()
            novo_nome = input("Digite o seu novo nome: ")
            pessoa.mudar_nome(novo_nome)
            print(f"O seu novo nome e {pessoa.nome}")
        
        elif opcao == 0:
            break 
        else:
            print("Opcao invalida.!")

    return pessoa 

pessoa = criar_pessoa() 
Limpar_tela()
print(f"\n---Seus dados--- ")
print(f"Nome: {pessoa.nome}")
print(f"Idade: {pessoa.idade}")
print(f"Peso: {pessoa.peso}")
print(f"Altura: {pessoa.altura}")




