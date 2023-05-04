from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView


def news_home(request):
    news = Articles.objects.order_by('-date')
    return render(request, 'news/index.html', {'news': news})


class newsDetailViev(DetailView):
    model = Articles
    template_name = 'news/detaul_vievs.html'
    context_object_name = 'artical'


class newsUpDate(UpdateView):
    model = Articles
    template_name = 'news/createNews.html'
    form_class = ArticlesForm


class newsDel(DeleteView):
    model = Articles
    success_url = '/news/'
    template_name = 'news/News_del.html'


def create_news(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_news')
        else:
            error = 'form is not valid'
    form = ArticlesForm
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/createNews.html', data)
