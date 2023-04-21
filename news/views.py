from django.shortcuts import render

def home(request):
    return render(request,'news/index.html')
    
def category(request):
    return render(request,'news/category.html')

def contact(request):
    return render(request,'news/contact.html')

def single_new(request):
    return render(request,'news/single.html')

