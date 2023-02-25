from django.shortcuts import render

def post_list(request):
    # En linux la barra es al reves!!!
    return render(request, 'blog\post_list.html', {})
