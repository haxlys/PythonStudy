from django.shortcuts import render

# Create your views here.
def post_list(requeset):
    return render(requeset, 'blog/post_list.html', {})
