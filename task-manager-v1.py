# toma uma função que é literalmente um print vazio

def separar():
    return print()

tasks = []
proximo_id = 1

print("""
    ====================================================================================================
    ||                                                                                                ||
    ||                              TASK MANAGER - Python                                             ||
    ||                                                                                                ||
    ====================================================================================================

                        [1] adicionar tarefa
                        [2] listar tarefas
                        [3]completar tarefas
                        [4] deletar tarefas
                        [5] sair
                        

""")

while True:

# separei os comandos pq ninguem merece ter que ver denovo toda hora

    separar()

    entrada = input ("selecione uma opção ([?] para ver os comandos):")

    separar()

    if entrada != "?" == True or int(entrada) < 1 or int(entrada) > 5:
         print("comando invalido, tente novamente")

    elif entrada == "?" :
        print("""

                        [1] adicionar tarefa
                        [2] listar tarefas
                        [3]completar tarefas
                        [4] deletar tarefas
                        [5] sair """)

    elif int(entrada) == 1:
            nome = input("adicione uma tarefa: ")
    
    
    
            task = {
                "id": proximo_id,
                "nome": nome,
                "status": "a fazer" 
            }
    
            tasks.append(task)
            proximo_id += 1
    
            separar()
    
            print(nome , "adicionado com sucesso" )
    
    elif int(entrada) == 2:
        for item in tasks:
            separar()
            print(f'{item["id"]}. {item["nome"]} | {item["status"]}')
    
    elif int(entrada) == 3:
        for item in tasks:
            separar()
            print(f'{item["id"]}. {item["nome"]} | {item["status"]}')
    
        concluir = int(input("qual tarefa voce deseja concluir: "))
    
        for item in tasks:
                    if concluir == item["id"]:
                        item["status"] = "concluído"
                        separar()
                        print("tarefa concluída com sucesso")
    
    elif int(entrada) == 4:
        for item in tasks:
            separar()
            print(f'{item["id"]}. {item["nome"]} | {item["status"]}')
    
        deletar = int(input("qual tarefa voce deseja apagar: "))
    
        for item in tasks:
            if deletar == item["id"]:
                tasks.remove(item)
                separar()
                print("tarefa apagada com sucesso")
    
    elif int(entrada) == 5:
        print("saindo do programa...")
        break