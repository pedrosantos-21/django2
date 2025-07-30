from django.shortcuts import render
from django.contrib import messages
# Import the ContatoForm from core.forms

from core.forms import ContatoForm

def index(request):
    """
    Render the index page.
    """
    return render(request, 'index.html')

def contato(request):
    form = ContatoForm(request.POST or None) #Quando o usuário enviar o formulário, o request.POST vai conter os dados do formulário ou Não!
    
    #is_valid() -> Verifica se o formulário foi preenchido corretamente
    #cleaned_data -> É um dicionário que contém os dados do formulário após a validação
                    #Se o formulário for enviado com o método POST e for válido, os dados
                    #serão processados e passado para a variável form.cleaned_data.
    
    if str(request.method) == 'POST'  and form.is_valid():
        nome = form.cleaned_data['nome']
        email = form.cleaned_data['email']
        mensagem = form.cleaned_data['mensagem']
        assunto = form.cleaned_data['assunto']
        
        print(f'Nome: {nome}, Email: {email}, Mensagem: {mensagem}, Assunto: {assunto} - Enviado com sucesso!')
        
        #messages -> é um recurso do Django para exibir mensagens ao usuário
        messages.success(request, 'Mensagem enviada com sucesso!')
        form = ContatoForm()  # Reseta o formulário após o envio
    else:
        messages.error(request, 'Erro ao enviar a mensagem. Por favor, tente novamente.')
    context = {
        'form': form
    }
    """
    Render the contact page.
    """
    return render(request, 'contato.html', context)

def produto(request):
    """
    Render the product page.
    """
    return render(request, 'produto.html')

