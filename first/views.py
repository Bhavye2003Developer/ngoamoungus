from django.shortcuts import render
from django.http import HttpResponse
from .models import DonarsInfo

# Create your views here.
def home(request):
    # return HttpResponse("working...")
    return render(request=request,template_name='first/homing.html')

def forms(request):
    # return HttpResponse("forms")
    if request.method == 'POST':
        firstname = request.POST['firstnameinput']
        lastname = request.POST['lastnameinput']
        email_address = request.POST['Emailinput']
        mobilenumberinput = request.POST['mobilenumberinput']
        state_input = request.POST['Stateinput']
        cityinput = request.POST['Cityinput']
        skillsets = request.POST['skillsetinput']
        # price = -1

        new_donar = DonarsInfo(first_name=firstname,last_name=lastname,email_address=email_address,phone_num=mobilenumberinput,state=state_input,city=cityinput,skill_set=skillsets)

        new_donar.save()
    return render(request,template_name="first/form.html")


def donars(request):
    if request.method == 'POST':
        firstname = request.POST['firstnameinput']
        lastname = request.POST['lastnameinput']
        email_address = request.POST['Emailinput']
        mobilenumberinput = request.POST['mobilenumberinput']
        state_input = request.POST['Stateinput']
        cityinput = request.POST['Cityinput']
        # skillsets = "No needed"
        # amt = request.POST['amt'] * request.POST['count_items']
        # if type_donate
        half_amt = request.POST['amt']
        count_items = request.POST['count_items']
        if (half_amt=='' or count_items==''):
            amt=0
        else:
            amt = int(half_amt) * int(count_items)
            
        # print(type(request.POST['amt']),type(request.POST['count_items']))

        new_donar = DonarsInfo(first_name=firstname,last_name=lastname,email_address=email_address,phone_num=mobilenumberinput,state=state_input,city=cityinput,price=amt)

        new_donar.save()

    return render(request=request,template_name="first/donation_form.html")