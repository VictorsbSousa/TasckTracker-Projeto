# Regras de Negocio: Validacao de dados para titulo e prioridades (Fase 2)
def cadastrar_tarefa(tarefas):
    print("\n--- Nova Tarefa ---")
    
    # Validação rigorosa do título (rejeita entradas vazias ou só com espaços)
    while True:
        titulo = input("Título da tarefa: ").strip()
        if titulo:
            break
        print("Erro: O título é obrigatório. Por favor, introduz um título válido.")

    descricao = input("Descrição da tarefa (opcional): ").strip()

    # Validação estrita da prioridade
    while True:
        prioridade = input("Prioridade (Alta, Média, Media, Baixa): ").strip().capitalize()
        if prioridade in ["Alta", "Média", "Media", "Baixa"]:
            break
        print("Erro: Prioridade inválida. Aceita apenas Alta, Média ou Baixa.")

    data_limite = input("Data Limite (Ex: DD/MM/AAAA): ").strip()

    # O status é definido automaticamente no momento do registo
    tarefa = {
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "data_limite": data_limite,
        "status": "Pendente"
    }
    
    tarefas.append(tarefa)
    print("Sucesso: Tarefa cadastrada com sucesso!")

def visualizar_tarefas(tarefas):
    # Tratamento para lista vazia
    if not tarefas:
        print("\nNão existem tarefas cadastradas no momento.")
        return

    # Iteração e exibição de lista preenchida organizada no terminal
    print("\n--- Lista de Tarefas ---")
    for i, tarefa in enumerate(tarefas, 1):
        print(f"\n[ Tarefa {i} ]")
        print(f"Título: {tarefa['titulo']}")
        print(f"Descrição: {tarefa['descricao']}")
        print(f"Prioridade: {tarefa['prioridade']}")
        print(f"Data Limite: {tarefa['data_limite']}")
        print(f"Status: {tarefa['status']}")
    print("-" * 24)

def main():
    tarefas = []
    # Menu de navegação contínuo
    while True:
        print("\n=== Menu TaskTracker ===")
        print("1. Cadastrar nova tarefa")
        print("2. Visualizar tarefas cadastradas")
        print("3. Sair da aplicação")
        
        opcao = input("Escolhe uma opção: ").strip()

        if opcao == '1':
            cadastrar_tarefa(tarefas)
        elif opcao == '2':
            visualizar_tarefas(tarefas)
        elif opcao == '3':
            print("A encerrar o TaskTracker. Até breve!")
            break
        else:
            print("Erro: Opção inválida. Escolhe 1, 2 ou 3.")

if __name__ == "__main__":
    main()
