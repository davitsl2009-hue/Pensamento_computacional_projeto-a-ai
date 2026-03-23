'''

CRUD

Açai

um aplicativo fast food, onde voce pode pedir sua sobremesa, personalizar o seu açai, efetuar o seu pagamento
e acompanhar o seu pedido

'''

print('\n=== SITE AÇAI===')
print('1. Fazer Pedido')
print('2. Entrar em contato com o suporte')
print('3. Mudar Pedido')
print('4. Cancelar Pedido')
print('0. Sair')

while True: 

    escolha_cliente = input('O que você deseja fazer?')

    if escolha_cliente == '1':
        print('\nVamos começar o seu pedido!')

        nome_cliente = input('Digite seu nome:')
        print('\nAqui está o cardápio.')

        print('1 - Açai 300ml (10R$)')
        print('2 - Açai 500ml (20R$)')
        print('3 - Açai 1L (30R$)')
        

        pedido_cliente = input('\nQual número do cardápio você gostaria de pedir? ')

        if pedido_cliente == '1':
            print('Você escolheu o açai de 300ml.')

        elif pedido_cliente == '2':
            print('Você escolheu o açai de 500ml.')

        elif pedido_cliente == '3':
            print('Você escolheu o açai de 1 litro.')

        else:
            print('Você escolheu uma opção invalida.')

        complemento_cliente = input('\nGostaria de adicionar algum complemento? (sim/não) +5R$')

        if complemento_cliente == 'sim':
            print('1. Ovomaltine')
            print('2. Leite Condensado')
            print('3. Paçoca')
            print('4. Nutella')
            print('5. Morango')

            açai_complemento = input('\nDigite o número do complemento desejado: ')

            if açai_complemento == '1':
                print('Você escolheu o ovomaltine como complemento.')
                preco_complemento = 5
                
            elif açai_complemento == '2': 
                print('Você escolheu o leite condensado como complemento.')
                preco_complemento = 3

            elif açai_complemento == '3':
                print('Você escolheu a paçoca como complemento.')
                preco_complemento = 2

            elif açai_complemento == '4':
                print('Você escolheu a nutella como complemento.')
                preco_complemento = 4

            elif açai_complemento == '5':
                print('Você escolheu o morango como complemento.')
                preco_complemento = 2
        else:
            print('Nenhum complemento adicionado ao seu pedido.')
            

        print('1. Cartão de débito')
        print('2. Cartão de crédito')
        print('3. Pix')

        forma_pagamento = input('\nDigite o número da forma de pagamento desejada: ')

        if forma_pagamento == '1':
            print('Você escolheu a opção de cartao de débito.')
        
        elif forma_pagamento == '2':
            print('Você escolheu a opção de cartão de crédito.')

        elif forma_pagamento == '3':
            print('Você escolheu a opção de Pix, pague com essa chave: 12345678900.')

        endereco_cliente = input('\nNos informe em qual endereço será entregue o pedido: ')
        
        confirmar_endereco = input(f'O endereço: {endereco_cliente} está correto?')

        if confirmar_endereco == 'sim':
            print('Seu Pedido foi confirmado')
        else:
            print('Faça seu Pedido novamente.')
    

    elif escolha_cliente == '2':
        print('\nCaso queira entrar em contato com o suporte, por favor envie um email para: suporte@açai.com ou ligue para (11) 1234-5678.')
        break

    elif escolha_cliente == '3':
        mudar_pedido = input('Oque você deseja mudar no seu pedido?')
        pedido_final = input(f'O pedido: {mudar_pedido} esta correto?')

        if pedido_final == 'sim':
            print('Seu Pedido foi modificado com sucesso!')
        
        else:
            print('Tente novamente retornando ao menu.')


    elif escolha_cliente == '4':
        cancelar_pedido = input('Você gostaria de cancelar seu pedido?')

        if cancelar_pedido == 'sim':
            print('Seu Pedido foi cancelado com sucesso!')

        else:
            print('Seu Pedido não foi cancelado.')


    elif escolha_cliente == '0':
        print('Saindo do Site. Volte Sempre!')
        break
    
    else:
        print('Opção invalida. Por favor tente novamente.')

