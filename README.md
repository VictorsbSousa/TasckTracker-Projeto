# TaskTracker - Sistema de Gestão de Tarefas em CLI

Projeto desenvolvido para o **Bootcamp II - Conteinerização, Orquestração e Deploy**. O sistema consiste numa aplicação CLI interativa desenvolvida em Python e empacotada através de Docker e Docker Compose.

---

## 🛠️ Comandos de Execução Rápida

### 1. Como construir a imagem Docker
```bash
docker build -t tasktracker-app .
```

### 2. Como executar o contentor em modo isolado/interativo
```bash
docker run -it tasktracker-app
```

### 3. Como executar via orquestração (Recomendado)
```bash
docker compose run tasktracker-app
```

---

## 📁 Estrutura do Repositório

* `src/main.py`: Ficheiro principal da aplicação Python com lógica interativa e validações de regras de negócio da Fase 2.
* `Dockerfile`: Configuração de criação da imagem leve baseada em `python:3.11-slim`.
* `docker-compose.yml`: Orquestração que habilita os sinalizadores `stdin_open` e `tty` para suportar entradas interativas no terminal.
* `docs/planejamento_logico.pdf`: Documentação de arquitetura mantida da Fase 1.
* `.gitignore`: Configuração de exclusão de arquivos de cache, IDEs e ambientes virtuais.
