from django.contrib import admin
from blogs.models import BlogModel, BlogArchiveModel, BlogCategoryModel, BlogTags, AuthorBlogModel, CommentsModle

@admin.register(BlogModel)
class BlogModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'updated_at']

@admin.register(BlogArchiveModel)
class BlogArchiveModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'updated_at']

@admin.register(BlogCategoryModel)
class BlogCategoryModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'updated_at']

@admin.register(BlogTags)
class BlogTagsModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'updated_at']
    
    
@admin.register(AuthorBlogModel)
class AuthorBlogModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'updated_at']
    
@admin.register(CommentsModle)
class CommentsModleAdmin(admin.ModelAdmin):
    list_display = ['comment', 'created_at', 'updated_at']