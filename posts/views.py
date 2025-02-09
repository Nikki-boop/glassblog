import requests
from django.shortcuts import render
from django.http import JsonResponse
from glassblog.models import BlogPost

def fetch_ebay_listings(keywords="pyrex"):
    url = "https://svcs.sandbox.ebay.com/services/search/FindingService/v1"
    headers = {
        "X-EBAY-SOA-OPERATION-NAME": "findItemsByKeywords",
        "X-EBAY-SOA-SECURITY-APPNAME": "NicoleBo-sandbo-SBX-9decc3fe3-15af6936", # replace with your app id
        "X-EBAY-SOA-RESPONSE-DATA-FORMAT": "JSON",
    }
    params = {
        "keywords": keywords,
        "paginationInput.entriesPerPage": 10,
    }

    response = requests.get(url, headers=headers, params=params)
    data = response.json()

    items = data['findItemsByKeywordsResponse'][0]['searchResult'][0].get('item', [])
    return items

def home_view(request):
    latest_post = BlogPost.objects.order_by('-date_posted').first()
    query = request.GET.get('q', 'pyrex')
    ebay_listings = fetch_ebay_listings(query)
    
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({'ebay_listings': ebay_listings})
    
    return render(request, 'pages/home.html', {'latest_post': latest_post, 'ebay_listings': ebay_listings})

def about_view(request):
    return render(request, 'pages/about.html')

def contact_view(request):
    return render(request, 'pages/contact.html')