import requests
from django.shortcuts import render
from django.http import JsonResponse
from glassblog.models import BlogPost

def fetch_ebay_listings(keywords="pyrex"):
    print("Query", keywords)
    pageSize = 10
    url = f"https://api.ebay.com/buy/browse/v1/item_summary/search?q={keywords}&limit={pageSize}"
    token = "v^1.1#i^1#r^0#f^0#I^3#p^1#t^H4sIAAAAAAAAAOVYa2wUVRTu9gEWaIkRH0F/lAFEwZm9d6b7mnSXbN+F0gdba1tsmrszd9pp57GZe5d2RdK1aRqURFF/+EKpjyA+E5UAIRESYqJiSI1GgcTEiAISAqIRgYjRmW0p20p4dRObuH8299xzzz3fd86598wFyRn5S4eqh84VuGZmDydBMtvlgrNB/oy8ZYU52fPzskCagms4uSiZO5DzcwlBuhYTV2MSMw2Ci/p0zSBiShhk4pYhmoioRDSQjolIJTESXlUr8hwQY5ZJTcnUmKKa8iCDoMcXgIpU7IeyoPC8LTUu2Wwyg4zi4QUP5KNewWvP+rz2PCFxXGMQigwaZHjAe1jAsxA2AShCQQSQK/YKbUxRM7aIahq2CgeYUMpdMbXWSvP16q4iQrBFbSNMqCZcGakP15RX1DWVuNNshcZ4iFBE42TiqMyUcVEz0uL46tuQlLYYiUsSJoRxh0Z3mGhUDF9y5ibcH6W62McrsqJgGclyQOAzQmWlaemIXt0PR6LKrJJSFbFBVZq4FqM2G9FuLNGxUZ1toqa8yPlrjCNNVVRsBZmK0nBruKGBCdWpdkLhUpMlyJCjJtuwupyFMpYgkop9rN8fgF4BCGPbjNoaI3nSPmWmIasOZaSozqSl2PYZT2YGpDFjK9Ub9VZYoY4/6XrCJQY9fJsT0tEYxmmX4UQV6zYNRanhtfkfX02ppUbjFI9bmDyRIsiOdCymyszkyVQmjiVPHwkyXZTGRLe7t7eX6xU40+p08wBAd8uq2ojUhXXEpHSdWnf01WsvYNUUFAnbK4kq0kTM9qXPzlTbAaOTCXmgR/CAMd4nuhWaLP2XIA2ze2I9ZKo+sM8TCCAk8QgEkBTFmaiP0FiKuh0/cBQlWB1ZPZjGNCRhVrLzLK5jS5VFwaPwgl/BrOwNKGxxQFHYqEf2slDBGGAcjUoB//+nTK430SNYsjDNUKZnKMsbNV2qemRZeV2FN9DYoncr9cukJloFtc6wv7QlQrwa30pX97TwdT3B662FK4Iv01SbmSZ7/0wR4NR6ZkioNgnF8pTgRSQzhhtMTZUS0yvAgiU3IIsmIljTbMGUQIZjsZpMndQZgndDh8TNoc7k/fSf3E1XREWchJ1eqJz1xDaAYirn3D6cZOpuE9lth9updVvckfJ6SrhVu2edVqhtkKNoVXm02eRSkDmyVuIsTMy4ZffZXL3TfTWZPdiwbzNqmZqGrWY45WrW9ThFUQ1Pt7LOQIKraJpdtdAnBHjBK/inFjYpdZF2TLcjKXMHce7yG2yo3RM/7kNZqR8ccO0DA6492S4XKAGL4UKwYEbOg7k5c+YTlWJORQpH1E7D/ma1MNeDEzGkWtm3ZY0U1sqPVdeeTUbjOx/6fbk/qyDtbWG4Hdw1/rqQnwNnpz01gHsuz+TBuXcW8B7AQwggFABsAwsvz+bCO3LnffzTkq9ykk+dOXqon3tjoG1rorj7CVAwruRy5WXlDriyquq2fDO4O3/X3APMi0PbTh4UNpw69vDeg4OVVsGIdOTEyOl5VQ3r9PUNYHjL3ZW7/tD3XJy55JfCruP70YX7ejsejwyWjWwTE29XPL/m5U3nnz17pp9r3ug/AXLa2080r+yYNXB7/4KW+AN4/f25n++OfPD05k/B6ZKhLz95v+Pd16pl8uTSe29pHLnQ2N+6/e93fGd+DEXe+/o8x2+Vkn9uP9b9+ua1L+37obPluTkdBVzl+cU7V746+N0XG9lkSbDw2KxDvYc/hCu2v1Ambvv21ubi9o/Cfcerl55a99neMrvNPPlmz4HDv+1Ar+zoOZr/a+Nfb31fvcKq6j+HCjcMHtl//GL2omdmP9rqWTMay38AxKJuQfURAAA="
    headers = {
        "X-EBAY-SOA-OPERATION-NAME": "findItemsByKeywords",
        "X-EBAY-SOA-SECURITY-APPNAME": "NicoleBo-sandbo-PRD-1dec1ac47-88916303", # replace with your app id
        "X-EBAY-SOA-RESPONSE-DATA-FORMAT": "JSON",
        "X-EBAY-C-MARKETPLACE-ID":"EBAY_US",
        "Authorization": "Bearer " + token
    }
    params = {
        "keywords": keywords,
        "paginationInput.entriesPerPage": pageSize,
    }

    response = requests.get(url, headers=headers, params=params)
    data = response.json()

    response_items = data['itemSummaries']
    show_items = []

    for item in response_items:
        show_items.append({
            'title': item['title'],
            'price': item['price']['value'] + " " + item['price']['currency'],
            'image': item['thumbnailImages'][0]['imageUrl'],
            'url': item['itemWebUrl']
        })

    return show_items

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