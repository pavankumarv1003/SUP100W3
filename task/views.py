from django.shortcuts import render


def WeekPage(request):
    return render(request,'week.html')
def mondayPage(request):
    return render(request,'monday.html')
def tuesdayPage(request):
    return render(request,'tuesday.html')
def wednesdayPage(request):
    return render(request,'wednesday.html')
def thursdayPage(request):
    return render(request,'thursday.html')
def fridayPage(request):
    return render(request,'friday.html')
def saturdayPage(request):
    return render(request,'saturday.html')
def sundayPage(request):
    return render(request,'sunday.html')
