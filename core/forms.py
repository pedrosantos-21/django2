from django import forms # do django importamos forms

class ContatoForm(forms.Form): #Classe forms extende de forms.Form
    nome = forms.CharField(max_length=100, label='Nome') #Campo de texto
    email = forms.EmailField(label='Email') #Campo de email
    mensagem = forms.CharField(widget=forms.Textarea(), label='Mensagem') #Campo de texto especificado com o (widget de área) de texto
    assunto = forms.CharField(max_length=100, label='Assunto') #Campo de texto