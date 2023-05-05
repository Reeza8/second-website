from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import *
from datetime import *
from django.http import *
import pytz
from django.contrib import messages




def home(request):
    #newsletter
    if request.method == 'POST':
        form=NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your email saved succefully') 
            return HttpResponseRedirect('/')
        else:
            messages.success(request, 'Your email did not saved succefully') 


    news=News.objects.all()        
    tz_tehran = pytz.timezone('Asia/Tehran') 
    datetime_tehran = datetime.now(tz_tehran)
    for new in news:
        if(new.published_date<datetime_tehran):
            new.status=1
            new.save()
    news=News.objects.filter(status=1)
    latest_news=news.order_by('-counted_views')
    form=NewsLetterForm()
    content={'news':news , 'latest_news':latest_news,'form':form}
    
    return render(request,'news/index.html',content)
    
def category(request,**kwargs):
    #newsletter
    if request.method == 'POST':
        form=NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your email saved succefully') 
            return HttpResponseRedirect('/')
        else:
            messages.success(request, 'Your email did not saved succefully') 


    if kwargs.get('category')!=None:
        if kwargs['category'] == 'All':
            news=News.objects.filter(status=1)
            cat='All'
        else:
            news=News.objects.filter(category__name=kwargs['category'],status=1)
            cat=kwargs['category']
    if kwargs.get('date')!=None:
        news=News.objects.filter(status=1,created_date__day=kwargs['date'][8:10])
        cat='Date({})'.format(kwargs['date'][:10])
    if news.exists():  
        latest_news=News.objects.filter(status=1).order_by('-counted_views')
        content={'news':news ,'category':cat , 'latest_news':latest_news }
        return render(request,'news/category.html',content)
    else:
        return render(request, 'error404.html')


def contact(request):
    if request.method == 'POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your contact saved succefully') 
            return HttpResponseRedirect('/')
        else:
            messages.success(request, 'Your contact did not saved succefully') 
            return HttpResponseRedirect('/')
    form=ContactForm()

    return render(request,'news/contact.html',{'form':form})


def single_new(request,id):
    latest_news=News.objects.filter(status=1).order_by('-counted_views')
    s_news=get_object_or_404(News,pk=id,status=1)
    s_news.counted_views+=1
    s_news.save()
    content={'s_news':s_news,'latest_news':latest_news}
    return render(request,'news/single.html',content)

def search(request):
    news=News.objects.filter(status=1)
    if text:=request.GET.get('searched_text'):
        news=news.filter(content__contains=text)
    content={'news':news}        
    return render(request,'news/searched_content.html',content)        

def signup(request):
    print('omaaaaaad')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print('reeeeeeee')
        if form.is_valid():
            form.save()
            print('saveeeeeed')
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, 'You signup succefully') 
            return redirect('/')
        else:
            form = UserCreationForm()
            messages.error(request, 'not valid inputs Your password can’t be too similar to your other personal information.Your password must contain at least 8 characters.Your password can’t be a commonly used password.Your password can’t be entirely numeric.') 
    form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

   