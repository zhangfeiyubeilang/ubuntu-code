from django.contrib import admin
from .models import BlogArticle
# Register your models here.
class BlogArticleAdmin(admin.ModelAdmin):
    list_display = ('title','author','publish')#展示列的名称
    list_filter = ('publish','author')#过滤器以publish
    search_fields = ('title','body')#加一个搜索框，
    raw_id_fields = ('author',)#通过作者的id增加博客文档
    date_hierarchy = 'publish' #以publish 的date 的不同而分层
    ordering = ['publish','author']#排序


admin.site.register(BlogArticle,BlogArticleAdmin)
