from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BlogCategoryModel(models.Model):
    name = models.CharField(max_length=30)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        

class BlogArchiveModel(models.Model):
    name = models.CharField(max_length=30)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Archive'
        verbose_name_plural = 'Archives'
    
class BlogTags(models.Model):
    name = models.CharField(max_length=30)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        
class AuthorBlogModel(models.Model):
    name = models.CharField(max_length=30, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Author'
        
class BlogModel(models.Model):
    image = models.ImageField(upload_to="blog-images/")
    title = models.CharField(max_length=100)
    description = models.TextField()
    
    category = models.ManyToManyField(BlogCategoryModel, related_name="blog")
    blogarchive = models.ManyToManyField(BlogArchiveModel, related_name="blog")
    tags = models.ManyToManyField(BlogTags, related_name="blog")
    author = models.ForeignKey(AuthorBlogModel, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title 
    
    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'
    
    
class CommentsModle(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(BlogModel, on_delete=models.CASCADE, related_name='comments')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f"{self.comment} - {self.user} - {self.blog}"
    
    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'