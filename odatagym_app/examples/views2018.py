from django.shortcuts import render

from odatagym_app.settings import GOOGLE_API_KEY


def get_sardinia_svg_example(request):
    return render(request, 'sardinia_svg.html')

def get_banda_larga_2018(request):
    return render(request, 'bandalarga2018.html')




def get_sardinia_drugstores(request):
    return render(request, 'markers.html',
                  context={'google_api_key': GOOGLE_API_KEY})


def get_rome_accidents(request):
    return render(request, 'heatmap.html',
                  context={'google_api_key': GOOGLE_API_KEY})
