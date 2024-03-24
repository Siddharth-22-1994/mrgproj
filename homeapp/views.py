from django.shortcuts import render, redirect
from datetime import date
import random
from django.contrib import messages
from homeapp.models import db_store


def home_view(request):
    if request.method=="POST":
        name = request.POST["name"]
        dob=request.POST['dob']
        place=request.POST["place"]
        today = date.today()
        day=random.randint(1, 30)
        month=random.randint(1, 12) 
        yr = dob.split('-')[0]  
        year = random.randint(int(yr)+26, int(yr)+32)
        
        mrg_date=f"{day}-{month}-{year}"
        
        try:
            name_uppre=name.upper()
            name_lower = name.lower()
            name_cap=name.capitalize()
            name_title = name.title()
            
            place_upper=place.upper()
            place_lower = place.lower()
            place_cap=place.capitalize()
            place_tit = place.title()
                 
            name_list = [name_uppre, name_lower, name_cap, name_title, name]
            place_list=[place_upper, place_lower, place_cap, place_tit, place]
                        
            db_get=db_store.objects.get(date=dob)
            if (db_get.name in name_list) and (db_get.place in place_list):
                print("-----------------------------> yes")
                messages.success(request, db_get.domrg)
                return redirect('homepage')
            else:
                db_data= db_store.objects.create(name=name, date=dob, place=place, domrg=mrg_date)
                db_data.save()
                messages.success(request, mrg_date)
                return redirect('homepage')
        except:
            lst1_name=["Keerthi", "keerthi", "KEERTHI", "Kancharla keerthi", 'kancharla keerthi', "KANCHERLA KEERTHI"]
            lst1_place=["kurnool", "Kurnool", "KURNOOL"] 
            
            lst2_name = ["siddharth", "Siddharth", "SIDDHARTH", "sidhu", "Sidhu", "SIDHU"]
            lst2_place=["cbe", "Cbe", "CBE", "coimbatore", "Coimabtore","COIMBATORE"]
            if ((name in lst1_name) and (place in lst1_place)):
                mrg_date="22-8-2025 $😍"
                db_data= db_store.objects.create(name=name, date=dob, place=place, domrg=mrg_date)
                db_data.save()
                messages.success(request, mrg_date)
                return redirect('homepage') 
            
            elif ((name in lst2_name) and (place in lst2_place) and (dob=="1994-08-22")):
                mrg_date="To my Amu 😘😘😍🫂"
                messages.success(request, mrg_date)
                return redirect('homepage')
                 
            db_data= db_store.objects.create(name=name, date=dob, place=place, domrg=mrg_date)
            db_data.save() 
            messages.success(request, mrg_date)
            return redirect('homepage')
        
    return render(request, "index.html")
