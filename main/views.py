from django.shortcuts import render
from django.http import HttpResponse
# from .models import Ma_Works
from django.template.loader import render_to_string
# Create your views here.


def index(request ):
    selected_item = request.GET.get('item', 'default')
    
    data = { 'selected_item': selected_item}
    print(request.GET)
    return render(request, 'index.html' , data )

# def about(request):
#     return render(request , 'about.html')

# def home(request):
#     return render(request , 'home.html')

# def skills(request):
#     return render(request , 'skills.html')

# def works(request):
#     works = Ma_Works.objects.all()
#     return render(request , 'works.html' , {'works': works})

# def contact(request):
#     return render(request , 'contact.html')