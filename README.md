ProjetoTarso
ProjetoTarso é uma aplicação em Python com interface web que acessa o serviço de agendamento de salas do Microsoft Booking através da API do Microsoft Graph.

Como executar a aplicação
Antes de executar a aplicação, é necessário seguir as instruções de instalação e configuração listadas abaixo:

Crie uma conta de desenvolvedor na Microsoft e registre o aplicativo.
Acesse o site do Microsoft Azure e crie uma nova assinatura.
Registre a sua aplicação no painel de controle do Azure.
Instale as bibliotecas necessárias, como Flask, Microsoft Graph e suas dependências.
Para executar a aplicação localmente, siga os seguintes passos:

Clone o repositório do ProjetoTarso: git clone https://github.com/engffsantos/ProjetoTarso.git.
Crie um ambiente virtual para o seu projeto com o comando python3 -m venv venv.
Ative o ambiente virtual com o comando source venv/bin/activate (no Linux/Mac) ou venv\Scripts\activate (no Windows).
Instale as dependências do projeto com o comando pip install -r requirements.txt.
Execute a aplicação com o comando python app.py.
Acesse a aplicação em http://localhost:5000 no seu navegador.
Funcionalidades
O ProjetoTarso permite que os usuários realizem as seguintes funcionalidades:

Buscar salas disponíveis
Agendar uma sala
Editar um agendamento
Cancelar um agendamento
Tecnologias utilizadas
O ProjetoTarso utiliza as seguintes tecnologias:

Python 3
Flask
Microsoft Graph API
HTML
CSS
JavaScript
Contribuindo
Se você deseja contribuir para o ProjetoTarso, siga os seguintes passos:

Faça um fork do repositório.
Crie uma nova branch com as suas modificações: git checkout -b my-feature.
Realize as suas modificações e faça o commit: git commit -m "Minha nova funcionalidade".
Envie as suas modificações para a sua branch no repositório fork: git push origin my-feature.
Abra um pull request para a branch principal do repositório.
