# Projeto - Disciplina de Computação Paralela e Distribuída

## Desafio 1

### Sobre o desafio 1: 

#### Client
    - Nesta pasta foi criado um arquivo Dockerfile baseado na imagem Alpine, que é responsável por enviar requisições utilizando um script em loop para o servidor da pasta ./web, que contem o app.py.

#### Web
    - Nesta pasta foi criado o app.py, que é responsável por iniciar um servidor Flask, e expor uma rota "/" na porta 8080.
    - Também foi criado um Dockerfile, que instala o Flask dentro da imagem e que também roda o app.py.

#### docker-compose.yml
    - O docker-compose.yml é responsável por instanciar os serviços e a rede, que faz a conexão entre esses serviços. Quando o comando: "docker-compose up --build" é rodado no terminal, ambos os Dockerfile de client e web são executados.

---

## Desafio 2

### Sobre o desafio 2:

#### Database
    - Nesta pasta foi criado o Dockerfile e o init_db.py, o init_db.py é responsável por criar uma tabela no sqlite chamada 'usuarios' e depois inserir os 3 nomes na tabela de usuarios.
    - Também contém o Dockerfile, que é responsável por executar o arquivo init_db.py.

#### Reader
    - Na pasta /reader foi criado o read_data.py que tem como objetivo se conectar ao banco e rodar um comando 'SELECT' pra listar todos os nomes registrados na tabela do banco que foram inseridos.
    - No Dockerfile, foi atribuído apenas a responsabilidade de executar o arquivo read_data.py.

#### docker-compose.yml
    - No docker-compose.yml foram criados dois serviços (db e reader) e o volume (db_data_) que inicia automaticamente pelo Docker.
    - Dentro do serviço db_data, o volume do banco de dados é persistido, mesmo que o container seja "destruído" ou apagado.