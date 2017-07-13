from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Physician


def index(request):
    request.session["login"] = "false"
    return render(request, 'dashboard/index.html')

#TODO: log in with different kinds of users
def dashboard(request):
    if 'user_id' in request.session:
        first_name = request.session['first_name']
        context = {"username": first_name}
        return render(request, 'dashboard/dashboard.html', context)
    else:
        try:
            if request.method == 'POST':
                pid = request.POST['id']
                pwd = request.POST['pwd']
                physician = Physician.objects.get(physicianID=pid)
                if (pwd == physician.pPassword):
                    context = {"message":"Welcome, ","username": physician.physicianFirstName, "message2":"!"}
                    request.session['user_id'] = physician.physicianID
                    request.session['first_name'] = physician.physicianFirstName
                    request.session['last_name'] = physician.physicianLastName
                    request.session['phone_number'] = physician.physicianPhone
                    return render(request, 'dashboard/dashboard.html', context)
                else:
                    context1 = {"message":"Incorrect credentials! Check your login details."}
                    return render(request, 'dashboard/error.html', context1)
        except Physician.DoesNotExist:
            return HttpResponse("Error!")

def logout(request):
    try:
        del request.session['user_id']
        del request.session['first_name']
        del request.session['last_name']
        del request.session['phone_number']
        request.session['login'] = "false"
    except KeyError:
        pass
    return HttpResponse(render(request, 'dashboard/index.html'))