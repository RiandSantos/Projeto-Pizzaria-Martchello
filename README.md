![Badge em Desenvolvimento](http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=yellow&style=for-the-badge)



# 💡 Projeto-Semestral Pizzaria Martchello


# ⚙️ Linguagens do projeto: <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />  <img src="https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E)" />

## 🍕 Proposta de projeto: 
- Uma Pizzaria com chatbot, Os clientes consegue realizar o pedido desejado através do chatbot caso não tenha uma opção do seu agrado no nosso menu.




## 📋 Histórias

 ### 📁 Banco de dados:
- O usuario gostaria de cadastra-se no site;
- O usuario gostaria de logar no sistema com seu usuario e senha;
- O usuario gostaria alterar a sua senha;

 
 
 #### ⚙️ Para o ChatBot:
 
 
 1-pizza tamanho: pequeno|medio| grande. 👍
 
 2-Escolha quantos sabores desejar de 1 a 4. 👍
 
 3-Escolha o sabor 1 e se tiver escolhido 4 sabores, escolha 4 sabores da lista. 👍
 
 4-O Bot lança a lista de sabores de 1 a 10 (Se não tiver o sabor desejado, inserir no campo digitavel);
 
 5-Após a lista, deverá ter um campo para o cliente digitar o sabor desejado.
 
 6-formato de borda  recheada/tradicional.
 
 7-Lista de opções de recheios para borda.
 
 8-Endereço de entrega
 
 9-valor do pedido.
 
 10-forma de pagamento: pagamento na entrega/ no site
 
 11-pagamento: cartão,pix ou dinheiro
 
 12-Seu pedido está sendo feito  e jaja sai para entrega
 
 13-O prazo de entrega é de 40 minutos.
 
## Clone repositorio
```
$ git clone https://github.com/python-engineer/chatbot-deployment.git
$ cd chatbot-deployment
$ python3 -m venv venv
$ . venv/bin/activate
```
Install dependencies
```
$ (venv) pip install Flask torch torchvision nltk
```
Install nltk package
```
$ (venv) python
>>> import nltk
>>> nltk.download('punkt')
```
Modify `intents.json` with different intents and responses for your Chatbot

Run
```
$ (venv) python train.py
```
This will dump data.pth file. And then run
the following command to test it in the console.
```
$ (venv) python chat.py
```

Now for deployment follow my tutorial to implement `app.py` and `app.js`.

