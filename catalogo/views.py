from django.shortcuts import render

# Create your views here.
def index(request):
    obras = [
        {
            "id": 1,
            "titulo": "interestelar",
            "tipo": "filme",
        },
        {
            "id": 2,
            "titulo": "jujuland",
            "tipo": "serie",
        },
        {
            "id": 3,
            "titulo": "shrek",
            "tipo": "filme",
        }

    ]
    contexto = {
        "obras": obras,

    }
    
    return render(request, "catalogo/index.html", contexto)