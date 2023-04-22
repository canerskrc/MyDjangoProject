from django.http import HttpResponse
from django.shortcuts import render


def index(request):
      evenNumberList = [item for item in range(2, 45, 2)]
      return render(request, 'home/index.html', {'evenNumberList': evenNumberList})


def detail(request, detailNumber):
      return HttpResponse(f"{detailNumber}  detaylarını görüyorsunuz")

def archive(response, archiveNumber):
      return HttpResponse(f"Arşiv Numarası {archiveNumber}")


def comment(request, commentNumber):
      return HttpResponse(f"{commentNumber} numaralı yorumu okuyorsunuz.")
