from django.http import  HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'index.html')
    # return HttpResponse("Home ")

def ex1(request):
    s='''Navigation Bar <br> 
    <a href ="https://www.linkedin.com/in/nayeer-naushad-49ab83224/">My Linkedin</a> <br>
    <a href ="https://github.com/nayeer1169">My Github</a> <br>
    <a href ="https://nayeer1169.github.io/Personal_Portfolio/">My PortFolio</a> <br>
    <a href ="https://www.linkedin.com/in/nayeer-naushad-49ab83224/">My Linkedin</a> <br>
    <a href ="https://github.com/nayeer1169">My Github</a> <br>'''
    return HttpResponse(s)


def analyze(request):
    #get the text
    djtext= request.GET.get('text','default')   # this willl return u back whatever the text written in the code , in the treminal
    #check checkbox value
    removepunc = request.GET.get('removepunc','off')
    fullcaps = request.GET.get('fullcaps','off')
    newlineremover = request.GET.get('newlineremover','off')
    spacelineremover = request.GET.get('spacelineremover','off')
    Charcount = request.GET.get('Charcount','off')

    #check which checkbox is on
    if removepunc=="on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char 
        params = {'purpose' : 'Removed Punctuation' , 'analyzed_text' : analyzed}
        return render(request , 'analyze.html', params)
    elif fullcaps=="on":
        analyzed=""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose' : 'Change to UpperCase' , 'analyzed_text' : analyzed}
        return render(request , 'analyze.html', params)
    elif(newlineremover=="on"):
        analyzed=""
        for char in djtext:
            if char != "/n":
                analyzed = analyzed + char
        params = {'purpose' : 'Removes New Lines ' , 'analyzed_text' : analyzed}
        return render(request , 'analyze.html' , params)
    elif(spacelineremover=="on"):
        analyzed=""
        for index , char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                analyzed = analyzed + char
        params = {'purpose' : 'Removes New Lines ' , 'analyzed_text' : analyzed}
        return render(request , 'analyze.html' , params)
    # elif Charcount=="on":
    #     analyzed=""
    #     for char in djtext:
    #         analyzed=analyzed+char
    #     params = {'purpose': 'Character Counter', 'analyzed_text' : analyzed}
    #     return render(request , 'analyze.html' , params)

    else:
        return HttpResponse("Error")
    # # def capfirst(request):
#     return HttpResponse('''Capitalize First <br><button onclick= "window.history.back()">Go Back</button>''')
# def newlineremove(request):
#     return HttpResponse('''New Line Remove <br><button onclick= "window.history.back()">Go Back</button>''')
# def spaceremove(request):
#     return HttpResponse('''Space Remove <br><button onclick= "window.history.back()">Go Back</button>''')
# def charcount(request):
#     return HttpResponse('''Character Counter <br><button onclick= "window.history.back()">Go Back</button>''')
# def about(request):
#     return HttpResponse("about OTC")
# def display_txt(request):
#     file_path = '/Users/nayeer1169/Documents/Django/tutorial/tutorial/1.txt'z#     with open(file_path,'r') as file:
#         content = file.read()
#     return HttpResponse(f"<pre>{content}</pre>", content_type = "text/html")
