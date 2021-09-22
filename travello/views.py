from django.shortcuts import redirect, render
from .models import Destination

# Create your views here.
def index(request):
    
    dests = Destination.objects.all()

    return render(request,'index.html',{'dests': dests })

def adddestination(request):
    if request.method == 'POST':
        place_name = request.POST['place_name']
        description = request.POST['description']
        price = request.POST['price']
        offer = request.POST['offer']
        img =request.POST['filename']
        print(place_name,description,price,offer,img)
        obj = Destination(name=place_name, desc=description, price=price, offer=offer, img=img)
        obj.save()
        return redirect('/')
    else:
        return render(request,'adddestination.html')
