from django.shortcuts import render, HttpResponse, redirect
  # the index function is called when root is visited
def index(request):
    return render(request, 'surveyform/index.html')

def create(request):
    if request.method == "POST":
        print("*"*50)
        print(request.POST['name'])
        print(request.POST['language'])
        print(request.POST['location'])
        print(request.POST['comment'])
        request.session['name'] = request.POST['name']
        request.session['language'] = request.POST['language']
        request.session['location'] = request.POST['location']
        request.session['comment'] = request.POST['comment']
        return redirect("/result")
    else:
        return redirect("/")    
def result(request):
    data = {
        'name' : request.session['name'],
        'language' : request.session['language'],
        'location' : request.session['location'],
        'comment' : request.session['comment']
    }
    return render(request,'surveyform/result.html', data)
