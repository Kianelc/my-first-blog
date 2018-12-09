from django.db import models
from django.utils import timezone

# class é uma palavra-chave especial que indica que estamos definindo um objeto.
# Post é o nome do nosso modelo.
# models.Model significa que o Post é um modelo de Django, então o Django sabe ele que deve ser salvo no banco de dados.
class Post(models.Model):
    # models.CharField - é assim que definimos um texto com um número limitado de caracteres.
    # models.TextField - este campo é para textos sem um limite fixo. Parece ideal para o conteúdo de um blog, né?
    # models.DateTimeField - este é uma data e hora.
    # models.ForeignKey - este é um link para outro modelo.
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    # def significa que se trata de uma função/método e que publish é seu nome.
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    # Quando chamarmos __str__(), obteremos um texto (string) com o título do Post.
    # Dunder: double-underscore (__)
    def __str__(self):
        return self.title