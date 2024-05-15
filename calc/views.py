from django.shortcuts import render , HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator
from news.models import news
from registration.models import user_data
def calc1(request):
    c=""
    try:
        if request.method=="POST":
            n1=float(request.POST.get("num1"))
            n2=float(request.POST.get("num2"))
            opr=request.POST.get("opr")
            if opr=="+":
                c=n1+n2
            elif opr=="-":
                c=n1-n2
            elif opr=="/":
                c=n1/n2
            else :
                c=n1*n2

    except:
        c="INVALID OPRATIONS"
    print(c)
    data={
        "c":c,
        "n1":n1,
        "n2":n2,
        "opr":opr
    }
    return render(request, "calc.html",data )


def inti(n):
    n=str(n)
    a="1234567890."
    for i in n:
        if i not in a:
            return False
    return True


def even_odd(request):
    fn=""
    n=""
    try:
        if request.method=="POST":
            n=(request.POST.get("n"))
            print(n)
            print(type(n))
            n=int(n)
            if (n%2)==0:
               fn= "EVEN number"
            elif (n%2==1):
                fn="ODD number"
            else:
                fn ="not intiger"
 
    except:
        fn ="INVALIDs  "
    data={
        "fn":fn,
        "n":n
    }
    print(fn)
    return render(request , "even_odd.html", data)


def marksheet(request):
    total=0
    perc=0
    avg=0
    print(request.method)
    try:
        if request.method == "POST":
            n1=int((request.POST.get("num1")))
            print(n1)
            n2=int((request.POST.get("num2")))
            print(n2)
            n3=int((request.POST.get("num3")))
            print(n3)
            n4=int((request.POST.get("num4")))
            print(n4)
            n5=int((request.POST.get("num5")))
            total=n1+n2+n3+n4+n5
            avg=total/5
            perc=avg +"%"
            print(n1,n2,n3,n4,n5)
    except:
        pass
    
    print(total,avg,perc)
    data={
        "total":total,
        "perc":perc,
        "avg":avg
            }

    return render(request, "marksheet.html",data )
def service1(request):
    servicesdata=service.objects.all().order_by("-service_title")
    for a in servicesdata:
        print(a.service_icon) #it will print all icon names
    print(servicesdata)
    data={
        "servicesdata":servicesdata
    }
    return render(request, "service.html",data)
def news1(request):
    newsdata=news.objects.all()
    print(newsdata)
    data={
        "newsdata":newsdata,
    }
    return render(request, "news.html", data)
def newsdetails(request, slug):
    newsdetail=news.objects.get(news_slug=slug)
    print(slug)
    print(newsdetail.news_title)
    print
    data1={
        "newsdetail":newsdetail,
        #"newsid":news_slug
    }
    #print(data[newsid])
    return render(request, "newsdetails.html", data1)

def search(request):
    newsdetail=news.objects.all()
    try:
        if request.method=="POST":
            print("$%^")
            st=request.POST.get("equalsearch")
            print(st)
            if st!= None:
                print(st)
                newsdetail=news.objects.filter(news_title=st)
                
        if request.method=="POST":
            print("!23")
            stl=request.POST.get("likesearch")
            print(stl)
            if stl!= None:
                print(st)
                newsdetail=news.objects.filter(news_title__icontains=stl)
        
    except:
        print("errrorororororooro")
    #print(newsid)
    
    #print
    print(newsdetail, "111")
    print("stl", stl)
    print("st",  st)
    if newsdetail ==None:
        newsdetail=news.objects.all()
    print(newsdetail,"22")
    data1={
        "newsdetail":newsdetail,
        #"newsid":newsid
    }
    #print(data[newsid])
    return render(request, "search.html", data1)
    #return render(request , "search.html")
def paginator11(request):
    newsd=news.objects.all()
    try:
        if request.method=="POST":
            prev=request.POST.get("prev")
            print(type(prev),prev, "jamj")
            if prev:    
                print(prev)
    except:
        print("error")
    paginator=Paginator(newsd,2)
    page_number=request.GET.get("pagenumb")
    newsdatafinal=paginator.get_page(page_number)
    totalpage=newsdatafinal.paginator.num_pages
    if int(page_number)> 1 :    
        prev=int(page_number) -1
    else:
        prev=1
    if int(page_number)<int(totalpage):    
        next_page=int(page_number)+1
    else:
        next_page= totalpage
    #print(news)
    data={
        "newsd":newsdatafinal,
        "page_number":int(page_number),
        "prev":int(prev),
        "totalpage":int(totalpage),
        "next":int(next_page),
        "pp": [n+1 for n in range(int(prev))],
        "totalpagelist": [n+1 for n in range(totalpage)],
        "nn":[n+1 for n in range(int(page_number),int(totalpage))],
        "p1":int(1)
    }
    return render(request,"page.html",data)
def registraion(request):
    print(request.method)
    n=""
    try:
        if request.method=="POST":
            name=request.POST.get("name"),
            mobile=request.POST.get("mobile"),
            email=request.POST.get("email"),
            print(name, email)
            userdata=user_data(user_name=name, user_mobile=mobile, user_email=email)
            userdata.save()
            n="data inserted"
    except:
        print("errrorororooroorororo")
    return render(request, "registraion.html", {"n":n})
