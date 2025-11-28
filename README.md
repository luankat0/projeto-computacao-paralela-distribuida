## Projeto - Disciplina de Computação Concorrente, Paralela e Distribuída

Este repositório contém a resolução de 5 desafios propostos, focados em Docker, Docker Compose, Orquestração de Containers e Arquitetura de Microsserviços

### Desafio 1: Containers em Rede

#### Descrição da Solução e Arquitetura

O objetivo deste desafio foi estabelecer a comunicação entre dois containers distintos utilizando uma rede bridge customizada do Docker.

- **Serviço Web**: Uma aplicação Python (Flask) que expõe uma rota na porta 8080.
- **Serviço Client**: Um container baseado em Alpine Linux que executa um script em loop (`curl`), enviando requisições periódicas para o serviço Web.

#### Decisões Técnicas

A rede `app_net` foi criada no `docker-compose.yml` para isolar a comunicação. O DNS interno do Docker permite que o container `client` encontre o container `web` apenas pelo nome do serviço, sem necessidade de saber o endereço IP.

#### Estrutura dos Arquivos

- **Client**: Contém o Dockerfile que instala o `curl` e define o loop de requisições.
- **Web**: Contém o `app.py` (servidor Flask) e o Dockerfile para configurar o ambiente Python.
- **docker-compose.yml**: Orquestra a subida dos dois serviços e a criação da rede.

#### Instruções de Execução

1. Acesse o diretório do desafio: `cd desafio1`
2. Execute o comando: `docker-compose up --build`
3. O terminal exibirá os logs das requisições sendo feitas pelo cliente e recebidas pelo servidor.

---

### Desafio 2: Volumes e Persistência

#### Descrição da Solução e Arquitetura

Este desafio demonstra a persistência de dados utilizando volumes Docker, garantindo que as informações sobrevivam ao ciclo da vida dos containers.
- **Serviço DB**: Utiliza um script Python para criar um banco de dados SQLite e popular uma tabela `usuarios`. O arquivo do banco é salvo em um volume compartilhado.
- **Serviço Reader**: Conecta-se ao mesmo volume e realiza uma consulta `SELECT` para listar os dados inseridos.

#### Decisões Técnicas

Foi utilizado um **Volume Nomeado** (`db_data`) no `docker-compose.yml`. Isso desacopla os dados do container. Mesmo se o container `db` for removido, o arquivo `.db` permanece no volume. O serviço `reader` monta esse mesmo volume para acessar os dados, simulando uma persistência e compartilhamento de arquivos.

#### Estrutura de Arquivos

- **Database**: Contém `init_db.py` (criação e inserção de dados) e seu Dockerfile.
- **Reader**: Contém `read_data.py` (leitura de dados) e seu Dockerfile.
- **docker-compose.yml**: Define o volume `db_data` e o mapeia para o caminho `/data` dentro de ambos os containers.

#### Instruções de Execução

1. Acesse o diretório do desafio: `cd desafio2`
2. Execute o comando: `docker-compose up --build`
3. Verifique nos logs que o banco foi criado e, em seguida, os dados foram lidos pelo serviço Reader.

---

### Desafio 3: Orquestração de Serviços

#### Descrição da Solução e Arquitetura

Implementação de uma aplicação web que depende de serviços externos de bancos de dados e cache, orquestrados via Docker Compose.
- **Web**: Aplicação Flask principal.
- **DB**: Banco de dados PostgreSQL (imagem oficial).
- **Cache**: Banco de dados em memória Redis (imagem oficial).

#### Decisões Técnicas

Utilizou-se a diretiva `depends_on` para garantir que o Docker inicie os bancos de dados antes da aplicação web. No código da aplicação (`app.py`), foi implementada uma lógica de "retry" (tentativas de reconexão) para o PostgreSQL, garantindo robustez caso o banco demore alguns segundos a mais para estar pronto para aceitar conexões. O Redis é utilizado para contar visitas (dados efêmeros/rápidos) e o Postgres para dados relacionais.

#### Estrutura de Arquivos

- **Web**: Dockerfile para a aplicação Flask e instalação de bibliotecas (`psycopg2`, `redis`).
- **docker-compose.yml**: Instancia os três serviços, define variáveis de ambiente para o Postgres e configura a rede interna.

#### Instruções de Execução

1. Acesse o diretório do desafio: `cd desafio3`
2. Execute o comando: `docker-compose up --build`
3. Abra o navegador em `http://localhost:8080`. A cada atualização da página, o contador do cache será incrementado.

---

### Desafio 4: Microsserviços Independentes

#### Descrição da Solução e Arquitetura

Criação de dois microsserviços que se comunicam via protocolo HTTP (REST).
- **Serviço A (Produtor)**: API que disponibiliza uma lista de usuários em formato JSON.
- **Serviço B (Consumidor)**: Aplicação que consome a API do Service A, processa os dados e exibe uma resposta formatada em HTML.

#### Decisões Técnicas

A comunicação é síncrona. O Service B utiliza a biblioteca `requests` do Python para chamar o Service A. A resolução de nomes é feita pelo Docker: o Service B chama `http://service_a:5001`. Apenas a porta do Service B é exposta ao host para visualização final, mantendo o Service A acessível apenas internamente (embora pudesse ser exposto para debug).

#### Estrutura de Arquivos

- **Service A**: Código da API REST e Dockerfile.
- **Service B**: Código do consumidor e Dockerfile com dependência `requests`.
- **docker-compose.yml**: Define os dois serviços na mesma rede `micro_net`.

#### Instruções de Execução

1. Acesse o diretório do desafio: `cd desafio4`
2. Execute o comando: `docker-compose up --build`
3. Acesse `http://localhost:5002` no navegador para ver o resultado da comunicação entre os serviços.

---

### Desafio 5: Microsserviços com API Gateway

#### Descrição da Solução e Arquitetura

Implementação do padrão API Gateway para centralizar o acesso a múltiplos microsserviços.
- **Gateway**: Ponto único de entrada. Recebe as requisições externas e as roteia para o serviço apropriado.
- **Users Service**: Microsserviço interno que retorna dados de usuários.
- **Orders Service**: Microsserviço interno que retorna dados de pedidos.

#### Decisões Técnicas

A arquitetura foca na segurança e encapsulamento. No `docker-compose.yml`, apenas a porta do **Gateway** (8080) é mapeada para o host. Os serviços de Users e Orders não possuem portas expostas ("ports"), sendo acessíveis exclusivamente pelo Gateway através da rede interna do Docker. O Gateway atua como um Proxy Reverso simples.

#### Estrutura de Arquivos

- **Gateway**: Aplicação Flask que rota `/users` para o serviço de usuários e `/orders` para o de pedidos.
- **Users/Orders Service**: APIs simples em Flask.
- **docker-compose.yml**: Configuração da rede e exposição seletiva de portas.

#### Instruções de Execução

1. Acesse o diretório do desafio: `cd desafio5`
2. Execute o comando: `docker-compose up --build`
3. Testes as rotas através do Gateway:
    - Usuário: `http://localhost:8080/users`
    - Pedidos: `http://localhost:8080/orders`
4. A tentativa de acesso direto aos serviços internos (ex.: portas 3001 ou 3002) falhará, confirmando o isolamento da rede.