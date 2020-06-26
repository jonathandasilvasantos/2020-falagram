# Falagram

## O que é o Falagram?

Falagram é uma aplicação que permite gerar leituras em voz alta
das conversas ou grupos do Telegram.

## Dependências

Para utilizar o Falagram, é necessário instalar o 'sox'. Trata-se de uma biblioteca open source
para manipulação de áudio.

A instalação do sox é muito simples. No Linux (Ubuntu):

> sudo apt-get install sox

No macOS utilizando o gerenciador de pacotes brew:
> brew install sox

Para instalação no Windows, consulte o site:
[http://sox.sourceforge.net/](http://sox.sourceforge.net/)

## Instalação
Para instalar o Falagram, primeiramente clone o projeto:
``cd ~/
git clone https://github.com/jonathandasilvasantos/falagram.git``

Uma vez clonado o repositório, entramos em seu diretório e executamos sua instalação:
``cd Falagram
python3 setup.py install``

## Chave de acesso para a API do Telegram.
Antes de usar o Falagram, é preciso solicitar acesso à API do Telegram.
Para isso, acesso o link: [https://my.telegram.org/auth?to=apps](https://my.telegram.org/auth?to=apps) e cadastre uma aplicação desktop.

Com a API_ID e a API_HASH em mãos, basta adicioná-las como variáveis de ambiente.
Em linux e macOS isso pode ser feito executando no terminal:

``export FALAGRAM_API_ID="INSIRA SUA API_ID"
export FALAGRAM_API_HASH="INSIRA SUA API HASH"``

Legal, se tudo ocorreu bem você já pode rodar o Falagram!
Note: o primeiro uso do Falagram vai implicar na necessidade de adicionar no
prompt o número de seu telefone celular (ID do Telegram). Em seguida,
você receberá um código de verificação em seu Telegram que o permitirá
concluir o processo de login com sua conta do Telegram.

## Como usar

Para gerar um arquivo de áudio com as últimas conversas do grupo "Garoa Hacker Clube",
por exemplo, basta usar o comando 'history'.

`falagram history Garoa`

É necessário que você seja membro do grupo. A execução acima com o argumento 'garoa' vai fazer com que
o comando 'history' busque em suas conversas algum grupo (ou pessoa) que contenha no título o
termo 'garoa'. '

Para acompanhar em tempo real (ouvindo as mensagens enviadas) de uma conversa, utilize o comando 'listen'.

`falagram listen garoa`

## Licença
GNU General Public License v.3
