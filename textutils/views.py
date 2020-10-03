#i have created this file-chetan
from django.http import HttpResponse
from django.shortcuts import render #its use for templates rendering


def index(request):
        return render(request, 'index.html')

def analyze(request):
        djtext = request.POST.get('text','default')
        removepunc = request.POST.get('removepunc','off')
        removespace = request.POST.get('removespace', 'off')
        fullcaps = request.POST.get('fullcaps', 'off')
        newlineremove = request.POST.get('newlineremove', 'off')
        charactercount = request.POST.get('charactercount', 'off')
        removeextraspace = request.POST.get('removeextraspace', 'off')

        purpose = ""





    #check which checkbox is on
        if removepunc == 'on':
                punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
                analyzed = ""
                for char in djtext:
                        if char not in punctuations:
                                analyzed = analyzed + char
                params = {'purpose':'remove punctuations', 'analyzed_text':analyzed}
                purpose += " | remove punctuations"
                djtext = analyzed

        if removespace == 'on':
                space = " "
                analyzed = ""
                for char in djtext:
                        if char not in space:
                                analyzed = analyzed + char
                params = {'purpose':'remove space', 'analyzed_text': analyzed}
                djtext =analyzed
                purpose += " | remove space"

        if removeextraspace == 'on':
                analyzed = ""
                for index, char in enumerate(djtext):
                        if djtext[index] == " " and djtext[index+1] == " ":
                            pass
                        else:
                            analyzed = analyzed + char
                params = {'purpose':'remove extra space', 'analyzed_text': analyzed}
                djtext = analyzed
                purpose += " | remove extra space"


        if(fullcaps =="on"):
            analyzed =""
            for char in djtext:
                analyzed = analyzed + char.upper()
            params = {'purpose': 'change to uppercase', 'analyzed_text': analyzed}
            djtext = analyzed
            purpose += " | change to uppercase "

        if (newlineremove == "on"):
            analyzed = ""
            for char in djtext:
                if char!="\n" and char!="\r":
                    analyzed = analyzed + char
            params = {'purpose': 'remove new line', 'analyzed_text': analyzed}
            djtext = analyzed
            purpose += " | remove new line "

        if (charactercount == "on"):
            analyzed = 0
            for char in djtext:
                if char != "\n" and  char != " ":
                        analyzed = analyzed + 1
            params = {'purpose': 'count the no of char', 'analyzed_text': analyzed}
            purpose += " | count the no of char "

        params = {'purpose': purpose , 'analyzed_text': analyzed}


        if (removepunc!='on' and removespace!='on' and charactercount!='on' and newlineremove!='on' and fullcaps!='on' and removeextraspace!='on' ):
            return HttpResponse('ERROR OCCUR <br>please select any one option')


        return render(request, 'analyze.html', params)



def about(request):
    return HttpResponse ('about us')

