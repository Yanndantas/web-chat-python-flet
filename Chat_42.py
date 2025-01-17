# Tela inicial:
    # Título: Chat_42
    # Botão iniciar chat
        # Quando clicar no botão:
            # Abrir um PopUp/modal/alerta
                # Título: Bem vindo ao Chat_42
                # Caixa de texto: Escreva seu nome no chat
                # Botão: Entrar no chat
                    # Quando clicar no botão
                    # Sumir com o título
                    # Sumir com o botão Iniciar chat
                        # Carregar o chat
                        # Carregar o campo de enviar mensagem: "Digite sua mensagem"
                        #Botão de enviar
                            # Quando clicar no botão enviar
                            # Enviar a mensagem
                            # Limpar a caixa de mensagem

#!pip install flet #(Com o flet é possível fazer o front e o back-end) 

# Importando a biblioteca 
import flet as ft 

# Criar uma função principal para rodar o app

def iniciar(pagina):

    # Titulo
    titulo = ft.Text("Chat_42")
    
    def abrir_popup(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()
        print("Clicou no botão")

    # Websocket - tunel de comunicação entre dois usuários
    # 1- Criar função para construção do túnel
    # 2- Criar o tunel de comunicação 
    # 3- Anexar a funçao de enviar a mensagem pelo tunel a função de enviar mensagem
    def enviar_mensagem_tunel(mensagem):
        # Executar tudo o que acontece para todos os usuários
        texto_mensagem = ft.Text(mensagem)
        chat.controls.append(texto_mensagem)
        pagina.update

    pagina.pubsub.subscribe(enviar_mensagem_tunel)


    def enviar_mensagem(evento):
        nome_usuario = caixa_nome.value
        texto_campo_mensagem = campo_enviar_mensagem.value
        mensagem = f" {nome_usuario}: {texto_campo_mensagem}"
        pagina.pubsub.send_all(mensagem)
        # Limpando o campo de enviar mensagem após o envio 
        campo_enviar_mensagem.value = ""
        pagina.update()

    # Definindo os elementos visuais para enviar mensagens ao chat
    campo_enviar_mensagem = ft.TextField(label="Digite aqui sua mensagem")
    botao_enviar = ft.FilledButton("Enviar", on_click=enviar_mensagem)
    linha_enviar = ft.Row([campo_enviar_mensagem, botao_enviar])

    chat=ft.Column()

    def entrar_chat(evento):
        # Fechar popup
        popup.open=False
        # Sumir com o título
        pagina.remove(titulo)
        # Sumir com o botão Iniciar chat
        pagina.remove(botao_iniciar)
        # Carregar o chat
        pagina.add(chat)
        # Carregar o campo de enviar mensagem: "Digite sua mensagem"
        #Botão de enviar
        pagina.add(linha_enviar) # Adicionando o botão e o campo de texto na mesma linha definida acima 

        #Adicionar no chat a mensagem "usuário entrou no chat "
        nome_usuario = caixa_nome.value
        mensagem = (f"{nome_usuario} Entrou no chat")
        pagina.pubsub.send_all(mensagem)
        pagina.update()


    # Botao incial
    botao_iniciar = ft.FilledButton("Iniciar Chat", on_click= abrir_popup)
    
    
    #Criar popup

    # Definindo os elementos visuais do popup
    # Título: Bem vindo ao Chat_42
    titulo_popup = ft.Text("Bem vindo ao Chat_42")
    # Caixa de texto: Escreva seu nome no chat
    caixa_nome = ft.TextField(label="Digite o seu nome") #Label = orientação do que o usuário tem que preencher
    # Botão: Entrar no chat
    botao_popup = ft.FilledButton("Entrar no chat", on_click=entrar_chat)

    # Construindo o popup 
    popup = ft.AlertDialog(title=titulo_popup,
                           content=caixa_nome,
                           actions=[botao_popup])


# Elementos iniciais ao abrir a página
    # Colocar os elementos na pagina
    pagina.add(titulo)
    pagina.add(botao_iniciar)
    pagina.add(popup)




# Utilizando o flet para abrir o projeto como site
ft.app(iniciar, view= ft.WEB_BROWSER)