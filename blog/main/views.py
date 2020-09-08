from django.shortcuts import render

def main(request):
    context = { 'like' : 'Django很棒' }
    return render(request, 'main/main.html', context)
def about(request):
    return render(request, 'main/about.html')