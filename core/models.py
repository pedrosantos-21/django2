from django.db import models
from stdimage.models import StdImageField

#SIGNALS -> É uma ferramenta do Django que permite que você execute código em resposta a determinados
            # eventos, como a criação ou atualização de um modelo. Parecido com os eventos em JavaScript.
            # Por exemplo, você pode usar sinais para enviar um e-mail quando um novo usuário é criado
from django.db.models import signals
from django.template.defaultfilters import slugify

#SLUGIFY -> É uma função do Django que converte uma string em um formato amigável para URLs.
            # Por exemplo, "Meu Produto" se torna "meu-produto".
            #vai pegar o nome do produto e criar um slug a partir dele.
            
class Base(models.Model):
    criado = models.DateField('Data de Criação',auto_now_add = True)
    modificado = models.DateField('Data de Modificação',auto_now = True)
    ativo = models.BooleanField('Ativo', default = True)
    
    class Meta:
        abstract = True
        #abstract = True -> Significa que essa classe não será criada como uma tabela no banco de dados,
        # mas será usada como uma classe base para outras classes.

class Produto(Base):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', max_digits=10, decimal_places=2)
    estoque = models.IntegerField('Estoque', default=0)
    imagem = StdImageField('Imagem', upload_to='produtos', variations={'thumbnail': (200, 200)})
    slug = models.SlugField('Slug', max_length=100, unique=True, blank=True, editable=False)
    descricao = models.TextField('Descrição', blank=True, null=True)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return self.nome
    
def produto_pre_save(signal, sender, instance, **kwargs):
# O sinal pre_save é usado para definir o slug antes de salvar o produto no banco de dados.
    instance.slug = slugify(instance.nome)
    
#SIGNAL -> Conecta o sinal pre_save ao método produto_pre_save para que ele seja chamado antes de salvar um Produto.   
        # Quando o produto emitir o sinal pre_save, o método produto_pre_save será chamado.
signals.pre_save.connect(produto_pre_save, sender=Produto)
