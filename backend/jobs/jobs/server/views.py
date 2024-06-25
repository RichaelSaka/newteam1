from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
import json
import os
from pathlib import Path
from .. import filtering

# Create your views here.
def alljobs(request: HttpRequest):

    user = request.headers.get("username", None)
    if request.method == "POST":
        user_role = "software"
        data = json.loads(request.body)
        user = data.get("username", user)
        user_industries = data["industry"]
        predicate = filtering.get_predicate(user_industries, user_role)
        all_jobs = json.load("./jobs_data.json")
        filtered_jobs = list(filter(predicate, all_jobs))
        responseJSON = json.dumps(filtered_jobs)
        return HttpResponse(responseJSON)
    if request.method == "GET":
        # send job swiping page
        pageloc = "server/templates/card.html"
        rendered = render(request, pageloc)
        return rendered
        # template = render(request, "./templates/card.html", {})
        # return HttpResponse(template.render)

def login(request: HttpRequest):
    pass