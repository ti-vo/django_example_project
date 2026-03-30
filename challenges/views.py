from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

challenges_dict = {
    "january":"",
    "february": "",
    "march": ""
}

# Create your views here.
def monthly_challenge_by_number(request, month):
    return HttpResponse(month)

def monthly_challenges(request, month):
    challenge_text = challenges_dict.get(month)
    return HttpResponse(challenge_text)
    #return HttpResponseNotFound("this month is not supported")