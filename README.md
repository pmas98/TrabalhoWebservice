# Trabalho Webservice - API de Lista de Tarefas

Este é o projeto da AV3 da disciplina de Arquitetura de Sistemas, consistindo em uma API para gerenciamento de uma lista de tarefas.

Para executar esta API, siga estas etapas:

1. Clone o repositório para a sua máquina.
2. Instale as dependências necessárias executando `pip install -r requirements.txt` na pasta do projeto.
3. Execute as migrações do banco de dados com `python manage.py migrate`.
4. Inicie o servidor com `python manage.py runserver`.
5. Acesse http://127.0.0.1:8000/ no navegador ou envie requisições para essa URL.

Rotas disponíveis:

- **GetAllItems**: Retorna todas as tarefas - Método: GET - URL: http://127.0.0.1:8000/tasks/
  
- **CreateTask**: Cria uma nova tarefa - Método: POST - URL: http://127.0.0.1:8000/tasks/create
  
- **GetSingleItem**: Retorna uma tarefa com base no ID - Método: POST - URL: http://127.0.0.1:8000/tasks/<int:pk>
  
- **UpdateTask**: Atualiza uma tarefa com base no ID - Método: PATCH - URL: http://127.0.0.1:8000/tasks/<int:pk>/update/
  
- **DeleteTask**: Deleta uma tarefa com base no ID - Método: POST - URL: http://127.0.0.1:8000/tasks/<int:pk>/delete/
