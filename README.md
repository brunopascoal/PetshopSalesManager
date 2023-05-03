# PetshopSalesManager

![GitHub repo size](https://img.shields.io/github/directory-file-count/brunopascoal/PetshopSalesManager?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/top/brunopascoal/PetshopSalesManager?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/brunopascoal/PetshopSalesManager?style=for-the-badge)
![Bitbucket open issues](https://img.shields.io/bitbucket/issues/brunopascoal/PetshopSalesManager?style=for-the-badge)
![Bitbucket open pull requests](https://img.shields.io/bitbucket/pr-raw/brunopascoal/PetshopSalesManager?style=for-the-badge)

# Imagens

> Este é um sistema de gerenciamento de vendas para um petshop, que inclui uma interface de login e um CRUD (Create, Read, Update, Delete) para gerenciar vendas. A aplicação utiliza Docker para executar um servidor MySQL e possui duas tabelas no banco de dados: login e vendas_produtos.

### Ajustes e melhorias

O projeto ainda está em desenvolvimento e as próximas atualizações serão voltadas nas seguintes tarefas:

- [ ] Inserir aba de estoque;
- [ ] Inserir cadastro de usuario;
- [ ] Inserir coluna valor com base no valor e quantidade vendida;
- [ ] Otimização do processo;

## 💻 Pré-requisitos

Antes de começar, verifique se você atendeu aos seguintes requisitos:

<!---Estes são apenas requisitos de exemplo. Adicionar, duplicar ou remover conforme necessário--->

- Você instalou a versão mais recente de `Python 3.6 ou superior`
- Você tem uma máquina `<Windows / Linux / Mac>`
- Você leu `<guia / link / documentação_relacionada_ao_projeto>`.

## 🚀 Instalando PetshopSalesManager

Para instalar PetshopSalesManager, siga estas etapas:

### Clone o repositório:

```
git clone https://github.com/brunopascoal/PetshopSalesManager.git
```

### Entre no diretório do projeto:

```
cd PetshopSalesManager
```

### Crie e ative um ambiente virtual

Linux e macOS:

```
python -m venv venv
source venv/bin/activate
```

Windows:

```
python -m venv venv
venv\Scripts\activate
```

### Instale as bibliotecas necessárias:

```
pip install -r requirements.txt
```

## Inicie o servidor MySQL utilizando Docker

```
docker run --name petshop-mysql -e MYSQL_ROOT_PASSWORD=minha-senha-secreta -e MYSQL_DATABASE=petshop -p 3306:3306 -d mysql:latest
```

Certifique-se de substituir minha-senha-secreta pela senha desejada.

## ☕ Usando PetshopSalesManager

Para usar PetshopSalesManager, siga estas etapas:

1.Execute o script principal da aplicação:

```
python main.py

```

2.A interface de login será exibida. Insira suas credenciais de usuário e senha para acessar o sistema.

3.Após fazer login, você verá duas abas: "Estoque" e "Vendas". A aba "Estoque" permite gerenciar o estoque de produtos do petshop, enquanto a aba "Vendas" permite gerenciar as vendas realizadas.

4.Em cada aba, você pode adicionar, atualizar e excluir registros utilizando os botões "Adicionar", "Atualizar" e "Excluir", respectivamente.

5.Quando terminar de utilizar a aplicação, clique no botão "Logout" para sair e fechar a aplicação.

## 📫 Contribuindo para PetshopSalesManager

1. Bifurque este repositório.
2. Crie um branch: `git checkout -b <nome_branch>`.
3. Faça suas alterações e confirme-as: `git commit -m '<mensagem_commit>'`
4. Envie para o branch original: `git push origin PetshopSalesManager / <local>`
5. Crie a solicitação de pull.

Como alternativa, consulte a documentação do GitHub em [como criar uma solicitação pull](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

## 😄 Seja um dos contribuidores<br>

Quer fazer parte desse projeto? Clique [AQUI](CONTRIBUTING.md) e leia como contribuir.

## 📝 Licença

Esse projeto está sob licença. Veja o arquivo [LICENÇA](LICENSE.md) para mais detalhes.

[⬆ Voltar ao topo](PetshopSalesManager)<br>
