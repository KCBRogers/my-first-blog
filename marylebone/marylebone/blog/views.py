from django.shortcuts import render

# Create your views here.

def post_list(request):
    return render(request, 'blog/post_list.html', {})

def democracy(request):
    return render(request, 'blog/democracy.html', {})

def events(request):
    return render(request, 'blog/events.html', {})
