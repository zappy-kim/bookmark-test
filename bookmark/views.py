from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Bookmark

# Create your views here.

class BookmarkList(ListView):
    model = Bookmark
    # context_object_name = 'latest_list'
    paginate_by = 5
    # 한 페이지에 보여줄 개수를 정해준다.

class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name', 'url'] # 모델 속성
    success_url = reverse_lazy('list')

class BookmarkDetailView(DetailView):
    model = Bookmark

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    success_url = reverse_lazy('list') # 정상적으로 진행이 되면 리스트로 간다.
    template_name_suffix = '_update'

# class BookmarkDeleteView(DeleteView):
#     model = Bookmark
#     # template_name = 'bookmark_confirm_delete'
#     # fields = ['site_name', 'url']
#     success_url = reverse_lazy('list') # 정상적으로 진행이 되면 리스트로 간다.

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    fields = ['site_name', 'url']
    success_url = reverse_lazy('list')