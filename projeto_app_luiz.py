'''

CRUD

Açai

Um aplicativo fast food, onde você pode pedir sua sobremesa, personalizar o seu açai, efetuar o seu
pagamento e acompanhar o seu pedido.

'''


print('\n== SITE AÇAi==')
print('1. Fazer pedido')
print('2. Ver Meus Pedidos')
print('3. Mudar Pedido')
print('4. Cancelar Pedido')
print('5. Relátorio do Pedido')
print('0. Sair')

while True:

    escolha_cliente = input('O que você deseja fazer?')

    if escolha_cliente == '1':
        print('Vamos começar o seu pedido!')
        nome_cliente = input('Digite seu nome:')
        pedido_cliente = input('Descreva como você quer o seu açaí e o tamanho dele:')

    elif escolha_cliente == '2':
        print('Aqui esta seus pedidos:')

    elif escolha_cliente == '3':
        print('O que você deseja mudar no seu pedido?')
                
    elif escolha_cliente == '4':
        print('Seu Pedido foi cancelado!')

    elif escolha_cliente == '5':
        print('Aqui esta o relátorioo do seu pedido.')

    elif escolha_cliente == '0':
        print('Saindo do site. Até logo!')
        break

    else:
        print('Opção invalida. Por favor tente novamente.')