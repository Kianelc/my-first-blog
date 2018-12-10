from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

# Como você pode ver, nós criamos uma função (def) chamada 
# post_list que recebe um request, executa a função render 
# que irá renderizar (montar) nosso modelo de acordo com o 
# template blog/post_list.html, e retorna (return) o resultado.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
