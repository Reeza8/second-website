from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from news.models import News,Category,NewsLetter,Contact


@admin.register(News)
class NewsAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('title' ,'author','counted_views','status','id','published_date','created_date')
    search_fields = ['title','content']
    list_filter = ('status',)
    empty_value_display = '-empty-'
    summernote_fields = ('content',)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('name','email','subject','created_date')
    list_filter = ('email',)
    search_fields = ('name','message')

  

admin.site.register(Category)
admin.site.register(NewsLetter)

    


