from django.shortcuts import render , HttpResponse
from .models import *

def index(request):
   data=book.objects.all()
   context={
      'books':data
   }
   if request.method == 'POST':
    if request.POST.get('title') and request.POST.get('desc'):#to make sure the filed is not empty
      post=book()
      post.title= request.POST.get('title')
      post.content= request.POST.get('desc')
      post.save()
   return render (request,"books_authors_app/index.html",context)
def view(request,book_id):
   context = {
      'books' : book.objects.get(id = book_id),
      'authors' : book.objects.get(id = book_id).author.all(),
      'all_authors' : author.objects.all(),
    } 
   return render(request,"view.html",context) 