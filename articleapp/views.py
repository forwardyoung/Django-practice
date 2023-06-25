from django.shortcuts import render

from django.views.generic import ListView
# Create your views here.
class ArticleListView(ListView):
    model = Article
    context_object_name = 'article_List'
    template_name = 'articleapp/list.html'
    paginate_by = 5
