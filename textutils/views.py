# I have created this file - Harmit
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def analyze(request):
    # get the text
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    capfirst = request.POST.get('capfirst', 'off')
    reverse = request.POST.get('reverse', 'off')
    spacerem = request.POST.get('spacerem', 'off')
    charcount = request.POST.get('charcount', 'off')
    upcase = request.POST.get('upcase', 'off')
    lowcase = request.POST.get('lowcase', 'off')
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    analyzed, txt = djtext, ""
    if removepunc == "on":
        for letter in djtext:
            if letter not in punctuations:
                txt += letter
        analyzed = txt
    if capfirst == "on":
        analyzed = analyzed.title()
    if reverse == "on":
        analyzed = analyzed[::-1]
    if spacerem == "on":
        analyzed = analyzed.replace(" ", "")
    if charcount == "on":
        count = f"<br><br>Count of characters is: <b>{len(analyzed)}</b>"
        analyzed += count
    if upcase == "on":
        analyzed = analyzed.upper()
    if lowcase == "on":
        analyzed = analyzed.lower()
    if removepunc != "on" and capfirst != "on" and reverse != "on" and spacerem != "on" and charcount != "on" and upcase != "on" and lowcase != "on":
        analyzed = "No command found"
    params = {
        'analyzed_text': analyzed,
        'purpose': djtext
    }
    return render(request, "analyze.html", params)


def about(request):
    return render(request, "about.html")
