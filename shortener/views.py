from django.shortcuts import render, redirect
from .models import ShortURL
from django.http import HttpResponseNotFound
import random, string
# Create your views here.
def index(request):
    if request.method == 'POST':
        original_url = request.POST.get('url')
        # Logic to create and save a short URL would go here
        # For now, we will just pass
        short_code = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        short_url = ShortURL.objects.create(original_url=original_url, short_code=short_code)
        return render(request, "shortener/index.html", {"short_url": short_url})
    return render(request, "shortener/index.html")

def redirect_url(request, short_code):
    try:
        link = ShortURL.objects.get(short_code=short_code)
        return redirect(link.original_url)  # Redirects to the original site
    except ShortURL.DoesNotExist:
        return HttpResponseNotFound("Sorry, this short link doesn't exist.")