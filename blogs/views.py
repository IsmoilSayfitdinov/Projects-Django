from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DeleteView
from blogs.models import BlogArchiveModel, BlogModel, BlogCategoryModel, BlogTags, AuthorBlogModel, CommentsModle
class BlogListView(ListView):
    template_name = "blog-list-left-sidebar.html"
    context_object_name = "blogs"
    model = BlogModel
    
    def get_queryset(self):
        qs = BlogModel.objects.all().order_by('-pk')
        cate = self.request.GET.get("category")
        tag = self.request.GET.get("tag")
        archive = self.request.GET.get("archive")
        
        if cate:
            qs = qs.filter(category=cate)
        if tag:
            qs = qs.filter(tags=tag)
        if archive:
            qs = qs.filter(blogarchive=archive)
        elif cate == False:
            return False
        elif tag == False:
            return False
        elif archive == False:
            return False
        return qs
    
    def get_context_data(self,  object_list=None  ,**kwargs):
        conetxt = super().get_context_data(**kwargs)
        conetxt.update( {
            
            "category": BlogCategoryModel.objects.all(),
            "tags": BlogTags.objects.all(),
            "archives": BlogArchiveModel.objects.all(),
            "author": AuthorBlogModel.objects.all()
        })
        
        return conetxt


class BlogDeatilView(DeleteView):
    model = BlogModel
    template_name = "blog-details-left-sidebar.html"
    context_object_name = "blog_detail"
    
    def get_queryset(self):
        qs = BlogModel.objects.all().order_by('-pk')
        cate = self.request.GET.get("category")
        tag = self.request.GET.get("tag")
        archive = self.request.GET.get("archive")
        
        if cate:
            qs = qs.filter(category=cate)
        if tag:
            qs = qs.filter(tags=tag)
        if archive:
            qs = qs.filter(blogarchive=archive)
        elif cate == False:
            return False
        elif tag == False:
            return False
        elif archive == False:
            return False
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "categories": BlogCategoryModel.objects.all(),
            "tags": BlogTags.objects.all(),
            "archives": BlogArchiveModel.objects.all(),
            "authors": AuthorBlogModel.objects.all(),
        })
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        
        comment = request.POST.get("comment")
        
        if comment:
            CommentsModle.objects.create(comment= comment, user= request.user, blog= self.object)
            return render(request, self.template_name, self.get_context_data())