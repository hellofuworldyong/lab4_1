from django.shortcuts import render_to_response

# Create your views here.
from django.http import HttpResponse
from fyy.models import Author,Book

def search_author(request):
    return render_to_response('search_author.html')

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q=request.GET['q']
        author_id=Author.objects.filter(Name=q)
        books=Book.objects.filter(AuthorID=author_id)
        return render_to_response('search.html',{'books':books,'query':q})
    else:
        return HttpResponse('please submit a serach term.')

def book_detail(request):
    if 'authorid' in request.GET and request.GET['authorid']:
        authorid=request.GET['authorid']
        author=Author.objects.get(AuthorID=authorid)
        book=Book.objects.get(AuthorID=authorid)
        return render_to_response('book_detail.html',{'book':book,'author':author})
    else:
        return HttpResponse('please submit a serach term.')

def delete_book(request):
    if 'authorid' in request.GET and request.GET['authorid']:
        authorid=request.GET['authorid']
        book=Book.objects.get(AuthorID=authorid)
        book.delete()
        return render_to_response('delete_book.html')
        
    else:
        return HttpResponse('please submit a serach term.')
    
#change
