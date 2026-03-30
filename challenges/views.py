from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

challenges_dict = {
    "january": "Digital Detox: Spend one weekend without screens. Use the time to journal, read, or connect with loved ones in person.",
    "february": "Daily Yoga: Practice 15 minutes of yoga every day. Focus on breathwork and gentle stretches to start or end your day.",
    "march": "Mindful Eating: Cook one nourishing, plant-based meal per week. Explore new recipes and savor each bite without distractions.",
    "april": "Spring Cleaning for Good: Donate 10 items you no longer need to a local shelter or charity. Declutter your space and help others.",
    "may": "Gratitude Practice: Write down three things you’re grateful for every evening. Reflect on the small joys in life.",
    "june": "Outdoor Adventure: Spend at least 30 minutes outside daily—walk, hike, or simply sit in nature. Reconnect with the earth.",
    "july": "Act of Kindness: Perform one random act of kindness each week. It could be as simple as paying for someone’s coffee or volunteering an hour at a food bank.",
    "august": "Hydration Challenge: Drink 2 liters of water daily. Add lemon, cucumber, or mint for a refreshing twist.",
    "september": "Mindfulness Meditation: Meditate for 10 minutes every morning. Use apps or guided videos if you’re new to the practice.",
    "october": "Eco-Friendly October: Reduce waste by using reusable bags, bottles, and containers. Pick up litter in your neighborhood once a week.",
    "november": "Community Connection: Attend a local event or workshop. Meet new people and support community initiatives.",
    "december": None #"Reflection and Rest: Spend 10 minutes each day reflecting on the year. Prioritize rest and set intentions for the new year."
}

def index(request):
    list_items= ""
    months = list(challenges_dict.keys())
    return render(request, "challenges/index.html", {"months": months})

# Create your views here.
def monthly_challenge_by_number(request, month):
    months = list(challenges_dict.keys())
    if (month > len(months)) or (month <= 0):
        return HttpResponseNotFound("invalid month")
    forward_month = months[month-1]
    redirect_path = reverse("month_challenge", args=[forward_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenges(request, month):
    try:
        challenge_text = challenges_dict[month]
        return render(request, "challenges/challenge.html", {"text": challenge_text, 
                                                             "month_name": month})
    except:
        return HttpResponseNotFound("<h1>this month is not supported</h1>")