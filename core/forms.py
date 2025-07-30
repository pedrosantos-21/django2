from django import forms # do django importamos forms
from django.core.mail import EmailMessage # do django importamos a classe : EmailMessage

class ContatoForm(forms.Form): #Classe forms extende de forms.Form
    nome = forms.CharField(max_length=100, label='Nome') #Campo de texto
    email = forms.EmailField(label='Email') #Campo de email
    mensagem = forms.CharField(widget=forms.Textarea(), label='Mensagem') #Campo de texto especificado com o (widget de área) de texto
    assunto = forms.CharField(max_length=100, label='Assunto') #Campo de texto
    
    #método para enviar o e-mail, recuperando os dados do formulário e montamos o conteúdo do e-mail.
    def send_mail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']
        
        conteudo = f'Nome: {nome}\nE-mail: {email}\nAssunto: {assunto}\nMensagem {mensagem}'
        
        #instância o objeto da classe EmailMessage
        mail = EmailMessage(
            subject=f'Contato do site: {assunto}', # Assunto do e-mail
            body=conteudo, # Conteúdo do e-mail
            from_email='contato@seudominio.com.br', # E-mail do remetente
            to=['contato@seudomino.com.br',],# Lista de destinatários
            headers={'Reply-To': email}
        )
        #metodo para enviar o e-mail
        mail.send()