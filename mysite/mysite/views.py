from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')

def sites(request):
    s='''<a href="www.hackerrank.com">HackerRank</a><br> <a href="www.codechef.com">CodeChef</a><br><a href="www.hackerearth.com">HackerEarth</a>'''
    return HttpResponse(s)

def analyze(request):
    djtext = request.GET.get('text', 'default')
    rp = request.GET.get('removepunc', 'off')
    analysed=''
    rnl=request.GET.get('removenewline', 'off')
    cf=request.GET.get('capfirst','off')
    #purpose=[]
    if(rp == 'on'):
        #purpose.append("Remove Punctuations")
        puncs='''!@#$%^&*;',./:"\?'''
        for char in djtext:
            if char not in puncs:
                analysed=analysed+char
    djtext=analysed
    if(rnl == 'on'):
        #purpose.append("Remove New Line")
        analysed=""
        for char in djtext:
            if char == '/n' :
                analysed=analysed+' '
            analysed=analysed+char
    djtext=analysed
    if(cf =='on'):
        #purpose.append("Capitalise First Letter")
        analysed=""
        djtext=' '+djtext
        for i in range(0,len(djtext)):
            if(djtext[i]==' '):
                analysed=analysed+djtext[i]
                if djtext[i+1].islower():
                    anlysed=analysed+(djtext[i+1].upper())
                    i = i+1
                    continue
            analysed=analysed+djtext[i]
        djtext=analysed
    #p=[[]]
    params = {'t' : djtext}
    return render(request, 'analyze.html', params)
