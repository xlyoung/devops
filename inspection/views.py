from django.shortcuts import render



def inspection(request):
    return render(request, 'inspection/inspection.html')