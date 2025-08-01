from django.shortcuts import render
from django.contrib import messages
# Import the ContatoForm from core.forms

from core.forms import ContatoForm,ProdutoModelForm
from .models import Produto

def index(request):
    context = {
        'produtos': Produto.objects.all()  # Obtém todos os produtos do banco de dados
    }
    return render(request, 'index.html', context)

def contato(request):
    form = ContatoForm(request.POST or None) #Quando o usuário enviar o formulário, o request.POST vai conter os dados do formulário ou Não!
    
    #is_valid() -> Verifica se o formulário foi preenchido corretamente
    #cleaned_data -> É um dicionário que contém os dados do formulário após a validação
                    #Se o formulário for enviado com o método POST e for válido, os dados
                    #serão processados e passado para a variável form.cleaned_data.
    
    if str(request.method) == 'POST'  and form.is_valid():
        # Se o formulário for válido, chama o método send_mail para enviar o e-mail
        # com os dados do formulário.
       form.send_mail()
      
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
    if request.method == 'POST':
        form = ProdutoModelForm(request.POST, request.FILES)
        if form.is_valid():      
            
            form.save()  # Salva o produto no banco de dados
                        
            messages.success(request,'Produto cadastrado com sucesso!')
            form = ProdutoModelForm()
        else:
            messages.error(request, 'Erro ao cadastrar o produto. Verifique os dados e tente novamente.')
    else:
        form = ProdutoModelForm() #se não conrresponder ao método POST, exibe o formulário vazio e a mensagem de erro.
    # Renderiza o template 'produto.html' com o contexto que contém o formulário
    # para exibir na página.
    context = {
        'form': form
    }
    return render(request, 'produto.html', context)

