import requests
from django.shortcuts import render
from glassblog.models import BlogPost

def fetch_ebay_listings():
    url = "https://svcs.ebay.com/services/search/FindingService/v1"
    headers = {
        "X-EBAY-SOA-OPERATION-NAME": "findItemsByKeywords",
        "X-EBAY-SOA-SECURITY-APPNAME": 'YourAppIDHere', # replace with your app id
        "X-EBAY-SOA-RESPONSE-DATA-FORMAT": "JSON",
    }
    params = {
        "keywords": "glass",
        "paginationInput.entriesPerPage": 10,
    }

    response = requests.get(url, headers=headers, params=params)
    data = response.json()

    items = data['findItemsByKeywordsResponse'][0]['searchResult'][0].get ('item', [])
    return items
            

def home_view(request):
    latest_post = BlogPost.objects.order_by('-date_posted').first()
    ebay_listings = fetch_ebay_listings()
    return render(request, 'pages/home.html', {'latest_post': latest_post})

def about_view(request):
    return render(request, 'pages/about.html')

def contact_view(request):
    return render(request, 'pages/contact.html')