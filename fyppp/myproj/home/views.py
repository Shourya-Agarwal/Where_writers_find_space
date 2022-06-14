from django.shortcuts import render, HttpResponse
from datetime import datetime
from django.template import RequestContext
from home import keywords_define 
from home import img_scrapping

def index(request):
     name='Shourya'
     return render(request, 'index.html',{'name':name})

def newpage(request):
     if request.method=="POST":
          texts=request.POST.get('text_quote')
          username=request.POST.get('text_name')
          keyword=keywords_define.filter(texts)
          host=img_scrapping.Hottest()
          image_links=host.img_scrapper(keyword)
          context={
               'user_quote':texts,
               'user_name':username,
               'keywords':keyword,
               'all': image_links
          }
          return render(request, 'newpage.html', context)


