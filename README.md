# TrabalhoWebservice
Esse é o trabalho da AV3 da disciplina de Arquitetura de Sistemas. Essa é a API para uma lista de tarefas

Para rodar a API , siga essas etapas:

    Clone o repositório para a sua máquina.
    Instale as dependências necessárias rodando pip install -r requirements.txt na pasta do projeto.
    Rode o banco de dados com python manage.py migrate.
    Rode o servidor com python manage.py runserver.
    Navegue até http://127.0.0.1:8000/ no browser ou mande requests pra essa URL.

Rotas disponíveis:
  GetAllItems(Devolve todos as tarefas) - GET - http://127.0.0.1:8000/tasks/
  
  CreateTask(Cria uma nova tarefa) - POST - http://127.0.0.1:8000/tasks/create
  
  GetSingleItem(Devolve uma tarefa a partir do Id) - POST - http://127.0.0.1:8000/tasks/<int>pk>
  
  UpdateTask(Atualiza uma tarefa a partir do id) - PATCH - http://127.0.0.1:8000/tasks/<int>pk>/update/
  
  DeleteTask(Deleta uma tarefa a partir do id) - POST - http://127.0.0.1:8000/tasks/<int>pk>/delete/
