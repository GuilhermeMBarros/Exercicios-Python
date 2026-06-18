# Importação de funções específicas dos módulos.
# o comando from(origem) que indica de onde vem as funções,
# ou seja, de qual módulo você está extraindo as funções
# o comando import, indica quais funções você ira usar do(from)
# módulo carregado pelo comando from(origem)
from os import system,cpu_count,getenv       # Ctrl + espaço, para ver as funções dentro das bibliotecas
from math import sqrt,pow,pi                  
                                             
system("cls")                                
print("==== Origem OS ====")                               
print(cpu_count())                           
print("==== Origem math ====")                         
print(sqrt(49))                             
print(pow(2,5))                              
