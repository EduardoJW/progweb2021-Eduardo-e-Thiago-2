# progweb2021-Eduardo-e-Thiago-2

Repositório para o segundo trabalho de progweb. Desenvolvido por:

Eduardo Junqueira - 1710329

Thiago Avidos - 1611116

## Acesso
O acesso ao [site](https://card-maker-app.herokuapp.com/) se dá pelo link [https://card-maker-app.herokuapp.com/](https://card-maker-app.herokuapp.com/) .

## Conceito

O nosso projeto o card-maker foi criado para ajudar com a edição e salvamento de ideias de cartas para um jogo de cartas virtual, Summoner's Battlegrounds.
A ferramenta permite que os usuários criem e editem suas ideias de cartas para esse jogo, por enquanto a versão atual simplesmente salva as informações que compõem a carta, mas o plano é para o futuro integrar essa ferramenta com algum editor de imagens para assim rapidamente montar a carta em si.

## Desenvolvimento
Dentre as funcionalidades do site em relação as cartas todas as operações do CRUD estão implementadas, entre os usuários é possível criar usuários e logar com eles também é possível trocar sua senha, para cada usuário individual só é possível ver a interagir com as suas próprias cartas criadas, não é possível ver as cartas criadas por outros usuários. Cada usuário tem sua visão própria da lista de cartas e não é possível ver listas nem criar cartas se não estiver logado. Não implementamos o Ajax e também não implementamos a recuperação de senha. O Site está publicado através do Heroku.

## Manual do Usuário
* Primeiramente caso não tenha um usuário é preciso ir na opção da barra do topo e selecionar ["Registre-se"](https://card-maker-app.herokuapp.com/accounts/register/), após criar um usuário será possível logar pelo botão na própria barra do topo ["Login"](https://card-maker-app.herokuapp.com/accounts/login/). As funcionalidades não estarão operantes caso você não esteja logado.

* Após logar, na barra do topo estará indicado o nome do usuário logado atualmente. Agora o usuário pode acessar a ["Pagina Principal"](https://card-maker-app.herokuapp.com/) que leva para a página principal a qual tem botões que levam para as páginas de [criação](https://card-maker-app.herokuapp.com/CardMakerApp/cria/) e de [lista de cartas](https://card-maker-app.herokuapp.com/CardMakerApp/lista/).
* Na página de [criação](https://card-maker-app.herokuapp.com/CardMakerApp/cria/) é possível criar uma carta ao preencher o formulário e clicar em "Criar Carta". Não há limite rígido definido para quantas cartas podem ser criadas por usuário.
* Na página de [lista de cartas](https://card-maker-app.herokuapp.com/CardMakerApp/lista/) é possível visualizar a lista com as cartas criadas pelo usuário além de atualizar ou deletar as mesmas.
* É possível também trocar a senha do usuário em [Trocar Senha](https://card-maker-app.herokuapp.com/accounts/passwordChange/).

