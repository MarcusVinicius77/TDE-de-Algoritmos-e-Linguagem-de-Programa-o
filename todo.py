def criar_janela_inicial():
    return []

tarefas = criar_janela_inicial()

while True:
    print("\n=== LISTA DE TAREFAS ===")

    if len(tarefas) == 0:
        print("Nenhuma tarefa cadastrada.")
    else:
        for i, t in enumerate(tarefas, start=1):
            status = "[X]" if t["feito"] else "[ ]"
            print(f"{i}. {status} {t['texto']}")

    print("""
1 - Adicionar tarefa
2 - Marcar como concluída
3 - Editar tarefa
4 - Remover tarefa
5 - Resetar lista
6 - Sair
""")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        texto = input("Digite a tarefa: ")
        if texto.strip() != "":
            tarefas.append({"texto": texto, "feito": False})

    elif opcao == "2":
        num = int(input("Número da tarefa: "))
        if 1 <= num <= len(tarefas):
            tarefas[num - 1]["feito"] = True

    elif opcao == "3":
        num = int(input("Número da tarefa: "))
        if 1 <= num <= len(tarefas):
            novo = input("Novo texto: ")
            if novo.strip() != "":
                tarefas[num - 1]["texto"] = novo

    elif opcao == "4":
        num = int(input("Número da tarefa: "))
        if 1 <= num <= len(tarefas):
            tarefas.pop(num - 1)

    elif opcao == "5":
        tarefas = criar_janela_inicial()

    elif opcao == "6":
        break

    else:
        print("Opção inválida.")





