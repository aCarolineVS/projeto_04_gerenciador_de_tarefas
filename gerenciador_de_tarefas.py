import os
import json 

with open('tarefas.json', 'r', encoding='utf-8') as arquivo:
    tarefas = json.load(arquivo)

def mostrar_tarefas():
     barra = f'| {60*'-'}|'
     print(barra)
     for i in range(len(tarefas['tarefas'])):
         print(f'| {i+1} - Tarefa: {tarefas['tarefas'][i]} | Data: {tarefas['datas'][i]}')                          
         input('| Aperte ENTER para continuar...')
    

def adicionar_tarefa():
    barra = f'| {60*'-'}|'
    print(barra)
    print("| NOVA TAREFA")
    print(barra)
    tarefa = input("| Digite o nome da nova tarefa: ")
    data = input("| Informe a data: ")

    tarefas['tarefas'].append(tarefa)
    tarefas['datas'].append(data)

    with open('tarefas.json', 'w', encoding='utf-8') as arquivo:
       json.dump(tarefas, arquivo, indent=4, ensure_ascii=False)
    print(barra)
    print(f"| Tarefa ({tarefa}) adicionada com sucesso")
    input("| Aperte ENTER para continuar...")
    

def remover_tarefa():
    barra = f'|{60*'-'}|'
    print(barra)
    print("| REMOVER UMA TAREFA")
    for i in range(len(tarefas['tarefas'])):
        print(f'| {i+1} - Tarefa: {tarefas['tarefas'][i]} | Data: {tarefas['datas'][i]}')
    print(barra)
    
    try:
        id_tarefa = int(input("| Digite o número da tarefa que deseja remover: "))
        tarefa = tarefas['tarefas'].pop(id_tarefa-1)
        tarefas['datas'].pop(id_tarefa-1)
        print(f"| Tarefa ({tarefa}) removida com sucesso!")
        with open('tarefas.json', 'w', encoding='utf-8') as arquivo:
               json.dump(tarefas, arquivo, indent=4, ensure_ascii=False)
        input("| Aperte enter para continuar.")
    except:
        print("| Erro! Digite um número de tarefa válido.")
        input("| Aperte enter para continuar.")

def mostrar_menu():
    while True:
        os.system('cls')
        barra = f'|{60 *'-'}|'
        print(barra)
        print('| GERENCIADOR DE TAREFAS')
        print(barra)
        print('| 1 - Mostrar tarefas')
        print('| 2 - Adicionar tarefa')
        print('| 3 - Remover tarefa')
        print('| 4 - Sair')
        print(barra)
        opc = input('escolha uma opção:')
        if opc == '1': 
            os.system('cls')
            mostrar_tarefas()

        elif opc =='2':
            os.system('cls')
            adicionar_tarefa()

        elif opc == '3':
            os.system('cls')
            remover_tarefa()

        elif opc == '4':
            print('Saindo...')
            break

        else:
            print('ERRO! Favor informar uma opção valida' )
            input('| Aperte ENTER para continuar...')

mostrar_menu()
