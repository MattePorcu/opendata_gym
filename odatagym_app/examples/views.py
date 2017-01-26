from django.shortcuts import render

from odatagym_app.settings import GOOGLE_API_KEY


def get_sardinia_svg_example(request):
    return render(request, 'sardinia_svg.html')

def get_banda_larga_2015(request):
    return render(request, 'bandalarga2015.html')

def get_banda_larga_2018(request):
    return render(request, 'bandalarga2018.html')

def get_banda_larga_2020(request):
    return render(request, 'bandalarga2020.html')

def get_banda_larga(request):
    return render(request, 'bandalarga.html')

def get_ambulatori_pubblici(request):
    return render(request, 'ambulatoripubblici.html')

def get_ambulatori_privati(request):
    return render(request, 'ambulatoriprivati.html')

def get_ambulatori_totali(request):
    return render(request, 'ambulatoritotali.html')


def get_sardinia_drugstores(request):
    return render(request, 'markers.html',
                  context={'google_api_key': GOOGLE_API_KEY})


def get_rome_accidents(request):
    return render(request, 'heatmap.html',
                  context={'google_api_key': GOOGLE_API_KEY})
