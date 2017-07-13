from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from dashboard.models import Sample, Patient, Physician
import random


#Redirect to new_sample.html
def new_sample(request):
    Physiciandrop = Physician.objects.all()
    Patientdrop = Patient.objects.all()
    if 'user_id' in request.session:
        first_name = request.session['first_name']
        context = {"username": first_name,
                   "login": "true",
                   "Physiciandrop":Physiciandrop,
                   "Patientdrop":Patientdrop}
        return render(request, 'sampleManagement/new_sample.html', context)
    else:
        context = {"login": "false"}
        return render(request, 'sampleManagement/new_sample.html', context)



# Add new sample to database, return sample receipt
def sample_registration_receipt(request):
    if 'user_id' in request.session:
        first_name = request.session['first_name']
        patient_id = request.POST['newSample_patientID']
        patient_id_fk = Patient.objects.get(patientID=patient_id)

        # new code
        id = ''.join(random.choice('0123456789') for i in range(9))
        physician_id = request.POST['newSample_physicianID']
        physician_id_fk = Physician.objects.get(physicianID=physician_id)
        sample_category = request.POST['newSample_category']
        sample_disposition = request.POST['newSample_disposition']
        date_received = request.POST['newSample_dateReceived']
        sample = Sample.objects.create(patientID=patient_id_fk,
                                       physicianID=physician_id_fk,
                                       sampleID=id,
                                       sampleCategory=sample_category,
                                       sampleDisposition=sample_disposition,
                                       dateReceived=date_received)
        context = {"username": first_name,
                   "login": "true",
                   "sample_id": sample.sampleID,
                   "sample_disposition": sample.sampleDisposition,
                   "sample_Category": sample.sampleCategory,
                   "date_received": sample.dateReceived,
                   "date_test_done": sample.dateTestDone,
                   #"date_test_schedule": sample.testSchedule,
                   "patient_ID": sample.patientID.patientID,
                   "physician_ID": sample.physicianID.physicianID}
        # till here
        return render(request, 'sampleManagement/sample_registration_receipt.html', context)
    else:
        context = {"login": "false",
                   "msg": "Please login in."}
        return render(request, 'sampleManagement/sample_registration_receipt.html', context)


#Redirect to search_sample.html
def search_sample(request):
    Sampledrop = Sample.objects.all()
    if 'user_id' in request.session:
        first_name = request.session['first_name']
        context = {"username": first_name,
                   "login": "true",
                   'Sampledrop':Sampledrop}
        return render(request, 'sampleManagement/search_sample.html', context)

    else:
        context = {"login": "false"}
        return render(request, 'sampleManagement/search_sample.html', context)


#TODO: fetch sample info from database
def sample_info(request):

    #form = request.POST
    if 'user_id' in request.session:
        first_name = request.session['first_name']

        try:
            if request.method == 'POST':
                sid = request.POST['searchSample_sampleID']
                sample = Sample.objects.get(sampleID=sid)
                context = {"username": first_name,
                           "login": "true",
                           "sample_id": sample.sampleID,
                           "sample_disposition": sample.sampleDisposition,
                           "sample_Category": sample.sampleCategory,
                           "date_received": sample.dateReceived,
                           "date_test_done": sample.dateTestDone,
                           #"date_test_schedule": sample.testSchedule,
                           "patient_ID": sample.patientID.patientID,
                           "physician_ID": sample.physicianID.physicianID}
                return render(request, 'sampleManagement/sample_info.html', context)
        except Sample.DoesNotExist:
            return HttpResponse("Error!")
    else:
        context = {"login": "false"}
        return render(request, 'sampleManagement/sample_info.html', context)




def edit_sample(request):
    Sampledrop = Sample.objects.all()
    Physiciandrop = Physician.objects.all()
    Patientdrop = Patient.objects.all()
    if 'user_id' in request.session:
        first_name = request.session['first_name']
        context = {"username": first_name,
                   "login": "true",
                   "Sampledrop": Sampledrop,
                   "Patientdrop":Patientdrop,
                   "Physiciandrop":Physiciandrop
                   }
        return render(request, 'sampleManagement/edit_sample.html', context)
    else:
        context = {"login": "false"}
        return render(request, 'sampleManagement/edit_sample.html', context)



#Update a particular sample
def update_sample(request):
    if 'user_id' in request.session:
        first_name = request.session['first_name']
        try:
            if request.method == 'POST':
                sampleID = request.POST['editSample_sampleID']
                pID = request.POST['editSample_patientID']
                physicianID = request.POST['editSample_physicianID']
                category = request.POST['editSample_category']
                disposition = request.POST['editSample_disposition']
                dateReceived = request.POST['editSample_dateReceived']

                sample = Sample.objects.get(sampleID=sampleID)
                patient = Patient.objects.get(patientID=pID)
                physician = Physician.objects.get(physicianID=physicianID)
                sample.patientID = patient
                sample.physicianID = physician
                sample.sampleCategory = category
                sample.sampleDisposition = disposition
                sample.dateReceived = dateReceived
                sample.save()

                context = {}
                context['msg'] = "Success!"
                context['username'] = first_name
                return render(request, 'sampleManagement/sample_update_receipt.html', context)
        except Sample.DoesNotExist:
            return HttpResponse("Error!")



#Delete sample
def delete_sample(request):
    Sampledrop = Sample.objects.all()
    if 'user_id' in request.session:
        first_name = request.session['first_name']

        try :
            if request.method == 'POST':
                sid = request.POST['editSample_sampleID']
                sample = Sample.objects.get(sampleID=sid)
                sample.delete()
                context = {"username": first_name,
                           "login": "true",
                           "Sampledrop":Sampledrop,
                           "msg": "Deleted!"}
                return render(request, 'sampleManagement/sample_update_receipt.html', context)
        except Sample.DoesNotExist:
            return HttpResponse("Error!")
    else:
        context = {"login": "false"}
        return render(request, 'sampleManagement/sample_update_receipt.html', context)


    #dropdown
    def selectview(request):
        Sampledrop = Sample.objects.all()  # use filter() when you have sth to filter ;)
        form = request.POST  # you seem to misinterpret the use of form from django and POST data. you should take a look at [Django with forms][1]
        # you can remove the preview assignment (form =request.POST)
        if request.method == 'POST':
            selected_item = get_object_or_404(Item, pk=request.POST.get('Sample_id'))
            # get the user you want (connect for example) in the var "user"
            user.item = selected_item
            user.save()

            # Then, do a redirect for example

        return render_to_response('sampleManagement/search_sample', {'items': item}, context_instance=RequestContext(request), )