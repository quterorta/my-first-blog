import http

from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from  django.views.generic import DetailView, ListView
from .forms import CommentForm


def index(request):
    category_social = News.objects.all().filter(category__slug='social').order_by('-date')[:2]
    category_guides = News.objects.all().filter(category__slug='guides').order_by('-date')[:2]
    category_culture = News.objects.all().filter(category__slug='culture').order_by('-date')[:2]
    category_lifestyle = News.objects.all().filter(category__slug='lifestyle').order_by('-date')[:2]
    category_sex_and_love = News.objects.all().filter(category__slug='sex_and_love').order_by('-date')[:2]
    news = News.objects.order_by('-date')[:6]
    return render(request, 'main/index.html', {'news': news, 'category_social': category_social, 'category_guides': category_guides, 'category_culture': category_culture, 'category_lifestyle': category_lifestyle, 'category_sex_and_love': category_sex_and_love})

def about(request):
    return render(request, 'main/terms-of-use.html')

def social(request):
    category_social = News.objects.all().filter(category__slug='social').order_by('-date')
    return render(request, 'main/social.html', {'category_social': category_social})

def guides(request):
    category_guides = News.objects.all().filter(category__slug='guides').order_by('-date')
    return render(request, 'main/guides.html', {'category_guides': category_guides})

def culture(request):
    category_culture = News.objects.all().filter(category__slug='culture').order_by('-date')
    return render(request, 'main/culture.html', {'category_culture': category_culture})

def lifestyle(request):
    category_lifestyle = News.objects.all().filter(category__slug='lifestyle').order_by('-date')
    return render(request, 'main/lifestyle.html', {'category_lifestyle': category_lifestyle})

def sex_and_love(request):
    category_sex_and_love = News.objects.all().filter(category__slug='sex_and_love').order_by('-date')
    return render(request, 'main/sex_and_love.html', {'category_sex_and_love': category_sex_and_love})

class PostDetailView(DetailView):
    model = News
    template_name = 'main/view_post.html'
    # context_object_name = 'news'
    pk_url_kwarg = 'id'

    def post(self, request, *args, **kwargs):
        news_id = self.kwargs['id']
        post = News.objects.get(pk=news_id)

        if request.method == 'POST':
            # Комментарий был опубликован
            comment_form = CommentForm(data=request.POST)

            if comment_form.is_valid():
                # Создайте объект Comment, но пока не сохраняйте в базу данных
                new_comment = comment_form.save(commit=False)
                # Назначить текущий пост комментарию
                new_comment.post = post
                # Сохранить комментарий в базе данных
                new_comment.save()
                redirect_to = self.request.path
                return HttpResponseRedirect(redirect_to)
        else:
            comment_form = CommentForm()

        return render(request, {'post': post, 'new_comment': new_comment, 'comment_form': comment_form})

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        news_id = self.kwargs['id']
        context['comments'] = Comment.objects.all().filter(post=news_id, active=True)

        context['comment_form'] = CommentForm

        return context


class Search(ListView):

    context_object_name = 'search_results'
    template_name = 'main/search.html'
    def get_queryset(self):
        return News.objects.filter(title__icontains=self.request.GET.get("q")).order_by('-date')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['q'] = self.request.GET.get("q")
        return context


def cookie(request):
    return render(request, 'main/cookies.html')


def privacy_policy(request):
    return render(request, 'main/privacy-policy.html')


def terms_of_use(request):
    return render(request, 'main/terms-of-use.html')

