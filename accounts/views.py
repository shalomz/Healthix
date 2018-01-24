from django.shortcuts import render, redirect


def home(request):
    context = {}
    if request.user.is_authenticated():
        group = request.user.groups.get(user=request.user)
        if group:
            if group.name == "Accountants":
                templatename = 'accountants.html'
            elif group.name == 'Receptionists':
                templatename = 'receptionists.html'
            elif group.name == 'Doctors':
                templatename = 'home.html'
            elif group.name == 'LabTechs':
                templatename = 'lab_home.html'
            elif group.name == 'Admin':
                return redirect('/admin')
            elif group.name == 'Nurses':
                templatename = 'nurse-home.html'
            elif group.name == 'Surgeons':
                templatename = 'surgeon_home.html'
            elif group.name == 'Radiologists':
                templatename = 'radiology_home.html'
        else:
            templatename = 'home.html'
    else:
        templatename = 'landing.html'
    return render(request, templatename, context)
