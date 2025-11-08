# Projeto - Disciplina de Computação Paralela e Distribuída

## Desafio 1

### Sobre o desafio 1: 

#### Client
    - Nesta pasta foi criado um arquivo Dockerfile baseado na imagem Alpine, que é responsável por enviar requisições utilizando um script em loop para o servidor da pasta ./web, que contem o app.py

#### Web
    - Nesta pasta foi criado o app.py, que é responsável por iniciar um servidor Flask, e expor uma rota "/" na porta 8080
    - Também foi criado um Dockerfile, que instala o Flask dentro da imagem e que também roda o app.py

#### Docker-compose.yml
    - O docker-compose.yml é responsável por instanciar os serviços e a rede, que faz a conexão entre esses serviços. Quando o comando: "docker-compose up --build" é rodado no terminal, ambos os Dockerfile de client e web são executados.

