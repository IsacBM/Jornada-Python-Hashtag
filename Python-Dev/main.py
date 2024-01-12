# Titulo Hashzap
# Botão de Iniciar o chat
    #Popup
        # Bem vindo ao Hashzap
        #Escrever o nome
        # Entrar no chat

# Chat
#     Pessoa entrou no chat
#     Mensagens
# Campo para escrever a mensagem
# Botão de enviar - Tempo: 1:00:48
import flet as ft

def main(pagina):
    texto = ft.Text('HashZaps')
    
    nome_usuario = ft.TextField(label='Escreva seu nome:')
    chat = ft.Column()
    
    def enviar_mensagem_tunel(informacoes):
        chat.controls.append(ft.Text(informacoes))
        pagina.update()
    
    pagina.pubsub.subscribe(enviar_mensagem_tunel)
    
    def enviar_mensagem(evento):
        # Colocar o nome do usuario
        texto_campo_mensagem = f'{nome_usuario.value}: {campo_mensagem.value}'
        
        pagina.pubsub.send_all(texto_campo_mensagem)
        
        # Limpar o campo mensagem
        campo_mensagem.value = ''
        pagina.update()
    
    campo_mensagem = ft.TextField(label='Escreva sua mensagem aqui!', on_submit=enviar_mensagem)
    botao_enviar = ft.ElevatedButton('Enviar',on_click=enviar_mensagem)
        
    
    
    def fechar_popup(evento):
        popup.open = False
        pagina.update()
        
    def entrar_chat(evento):
        popup.open = False
        
        pagina.add(chat)
        
        linha_mensagem = ft.Row(
            [campo_mensagem, botao_enviar] 
        )
        
        pagina.add(linha_mensagem)
        texto = f'{nome_usuario.value} entrou no chat!'
        
        pagina.pubsub.send_all(texto)
        
        pagina.remove(botao_iniciar)
        pagina.update()
    
    popup = ft.AlertDialog(
        open=False,
        modal=True,
        title=ft.Text('Hashzaps'),
        content=nome_usuario,
        actions=[ft.ElevatedButton('Entrar', on_click=entrar_chat), ft.ElevatedButton('Fechar', on_click=(fechar_popup))]
        )
    
    def iniciar_chat(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()
        
    botao_iniciar = ft.ElevatedButton('Iniciar Chat', on_click=iniciar_chat)
    
    pagina.add(texto)
    pagina.add(botao_iniciar)
    
# ft.app(main)
ft.app(main, view=ft.WEB_BROWSER)
