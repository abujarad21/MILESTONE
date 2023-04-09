from django.shortcuts import render

from django.http import HttpResponse

from .models import Book
# Create your views here.
def index(request):
    return HttpResponse("Hello world \n safir hashikah")

def book_by_id(request,book_id):
    book=Book.objects.get(pk=book_id)
    return render(request, 'book_detail.html',{'book':book})