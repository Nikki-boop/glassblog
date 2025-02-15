import requests
from django.shortcuts import render
from django.http import JsonResponse
from glassblog.models import BlogPost

def fetch_ebay_listings(keywords="pyrex"):
    print("Query", keywords)
    pageSize = 10
    url = f"https://api.ebay.com/buy/browse/v1/item_summary/search?q={keywords}&limit={pageSize}"
    token = "v^1.1#i^1#I^3#f^0#p^1#r^0#t^H4sIAAAAAAAAAOVYW2wUVRju9sa1XgCBVEPWgYrQzuyZmc52Z9pd3FKgi6W3Lb2hKbMzZ9ppZ2eGOWdtSx9ca0QTxBhMJAqJTQjRQIjRiH2RS7w8KA+oGMWgL4RSQRKvRI01OjNdyrYSbt3EJu7L5pzzn/9833f+/5x/Dkjmz1m9o3rHbwWeWdlDSZDM9njoeWBOfl7xXTnZhXlZIM3AM5RckcwdzPmuAolxzRQaITINHUFvX1zTkeB2BomEpQuGiFQk6GIcIgFLQjS8qUZgKCCYloENydAIb6QqSMQUv8zzPJT9YllM8st2r37VZ5MRJJQYq0h8mVIqyZAPMLQ9jlACRnSERR0HCQYwHAkYkmabAC3QnMAEKA742wlvM7SQaui2CQWIkAtXcOdaaVhvDFVECFrYdkKEIuH10bpwpGpdbVOFL81XKKVDFIs4gSa31hoy9DaLWgLeeBnkWgvRhCRBhAhfaHyFyU6F8FUwdwDflbqMtQWOxUrL2ACECs9lRMr1hhUX8Y1xOD2qTCquqQB1rOL+mylqqxHrhhJOtWptF5Eqr/PXkBA1VVGhFSTWVYbbwvX1RKhWtQMKVhokEnU5ZpD1jVUkLUOJFqXSMjIQ4Gk/C9jUMuO+UiJPWWetocuqIxny1hq4EtqY4VRlQJoytlGdXmeFFezgSbdjUwqW8ny7s6Xje5jAXbqzqzBuy+B1mzfXf2I2xpYaS2A44WHqgCtQkBBNU5WJqYNuJKaCpw8FiS6MTcHn6+3tpXpZyrA6fQwAtK91U01U6oJxkXBtnVx37NWbTyBVl4oE7ZlIFXC/aWPpsyPVBqB3EiGO5lgOpHSfDCs0tfdfHWmcfZPzIVP5wTEBToK8KLOA4VklE+kRSkWoz4EBY2I/GRetHohNTZQgKdlhlohDS5UFllMYNqBAUvbzClnKKwoZ42Q/SSsQAghjMYkP/H+y5FbjPAolC+IMBXqGgrxBi0sbthdX1a7z8w2t8W6lrlhqwhtorTMcqGyNIr/GtOHGnlamtid4q6lwXfJrNdVWpsleP2MCOLmeERGqDYShPC16UckwYb2hqVL/zNpg1pLrRQv3R6Gm2R3TIhk2zUimDuoM0butQ+LOWGfyevpPrqbrskJOwM4sVs58ZDsQTZVybh9KMuI+Q7SrDp/o5Lqpdriop8VbtUvWGcXaJjnOVpXHa03KpUyhJyTKgshIWHaZTdU5xVeT0QN1+zbDlqFp0Gqmp53N8XgCizENzrS0zkCAq+IMu2rpMpYvBTzLBKbFS3Iv0o6ZdiRl8CDODd1ePe2b/G0fynJ/9KDnfTDoOZbt8YAKUEQvBw/m52zOzZlfiFQMKVVUKKR26vYnqwWpHthviqqVvTDr1F018lPVNVeSscRwy69rAlkFaU8LQ4+DpROPC3Ny6HlpLw3ggWsjefTdSwoYDjA0C2jartTbwfJro7n04txFzKcXTxbMHusYPb2PXmAcOPXM7IG5oGDCyOPJy8od9GT5tt8bkgu/qviy6PUdw0tbjiR/3HviyImNFWMlL6xqaFm5YdbuD4Hnvecv/PXR1o5XVmf/+ciL7wxUcJL58qHd+zpg0dydwZKHTtYNXCqeP3LmcuvyndnfHuu6wLXuL3mj+POHq/fuGp179OhQITf2RVvy7LK+4b1bNs1iR73e8vXk9pad765RNnb42w4uPF2df3zVkqyLH5utC3zdi6lt6ltfj/yy55PXIlfW1JxvvLytK3LluRW+Myfhm/Kh+X/fc+r8jnObn9zX3bjF/KzAujxc9+pLv4+VP7rqXPmlH5T7zj79TdHPe1oOvP3H1pqR7zcOtB9ulBYtUu9foT327Epi/7LjPzWPHB7+YFd5ycHR8b38B/8RoA/0EQAA"
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
   
    # Check if there is an error
    errors = data.get('errors', [])
    if errors:
        ## when token expires:
        """
        {'errors': [{'errorId': 1001, 'domain': 'OAuth', 'category': 'REQUEST', 'message': 'Invalid access token', 'longMessage': 'Invalid access token. Check the value of the Authorization HTTP request header.'}]}
        """
        print("Error", errors)
        return []
   
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