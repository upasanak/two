#i have created this
from django.http import HttpResponse
from django.shortcuts import render
#def index(request):
    #f = open("good.txt", "w+")
    #for i in range(6):
        #f.write("this is the line\n" % i+1)
    #return HttpResponse("<h1>hello upasana</h1>")
    #f.close()

#def about(request):
   # f = open("good.txt", "r+")
    #if f.mode == 'r+':
      #return HttpResponse(f.read())
    #f.close()
    #return HttpResponse("hello from about upasana")

#def access_url(request):
    #return HttpResponse('''<h1><a href = "https://www.Facebook.com/">Facebook </a></h1> \n
      #<h1><a href = "https://www.youtube.com/">youtube </a></h1>''')

def index(request):
    #dict = {"name": "upasana, gitanjali", "place": "Jupiter"}
    return render(request, "indexb.html")
    #return HttpResponse('''<h1><a href = "http://127.0.0.1:8000/about">About </a></h1> \n <h1><a href = "http://127.0.0.1:8000/access_url">Access URL </a></h1> ''')

def access_url(request):
    return HttpResponse('''Hello in access URL !!! \n <a href = "http://127.0.0.1:8000/">Home Page</a>''')

def analyseb(request):
    djtext = request.GET.get('text', 'default')
    djremovepunc = request.GET.get('removepunc', 'off')
    djcaps = request.GET.get('caps', 'off')
    djnlr = request.GET.get('nlr', 'off')
    djspacere = request.GET.get('spacere', 'off')
    djexspacere = request.GET.get('exspacere', 'off')
    djcharcount = request.GET.get('charcount', 'off')

    p = ''',./?><;':"{}[]-_)('''
    adjtext = ""

    #for removing punctuations
    if djremovepunc == "on":
        for i in djtext:
            if i not in p:
                  adjtext = adjtext + i

        dict = {"purpose": "Remove Punctuations", "atext": adjtext}
        return render(request, "anaylseb.html", dict)

    #for capitalization
    elif djcaps == "on":
        for i in djtext:
            adjtext = adjtext + i.upper()

        dict = {"purpose": "Capitalization", "atext": adjtext}
        return render(request, "anaylseb.html", dict)

    #fpr new line remover
    elif djnlr =="on":
        for i in djtext:
            if i != "\n":
                adjtext = adjtext + i

        dict = {"purpose": "New Line Remover", "atext": adjtext}
        return render(request, "anaylseb.html", dict)

    #for space reomval
    elif djspacere =="on":
        for i in djtext:
            if i != " ":
                adjtext = adjtext + i

        dict = {"purpose": "Space Remover", "atext": adjtext}
        return render(request, "anaylseb.html", dict)

    #remove extra space
    elif djexspacere == "on":
        for index, i in enumerate(djtext):
            if djtext[index] == " " and djtext[index+1] == " ":
                pass
            else:
                adjtext = adjtext + i

        dict = {"purpose": "Space Remover", "atext": adjtext}
        return render(request, "anaylseb.html", dict)

    # remove extra space
    elif djcharcount == "on":
        j = 0
        for i in djtext:
            if i != " ":
               j += 1

        dict = {"purpose": "Number Of Chacter is::", "atext": j}
        return render(request, "anaylseb.html", dict)

    else:
        return HttpResponse("<h1>Error!!!</h1>")
    #return HttpResponse('''Hello in about !!! \n <a href = "http://127.0.0.1:8000/">Home Page</a>''')

def about_us(request):
    return render(request, "about_us.html")

def contact_us(request):
    return render(request, "contact_us.html")