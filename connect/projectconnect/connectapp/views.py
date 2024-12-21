from django.shortcuts import render
from django.http import HttpResponse
import faker
from connectapp.models import Programmer, SoftwareDeveloper

fake = faker.Faker()





def starbucks_view(request):
    return render(request, 'homepage.html')

def adding_bulkdata_view(request):
    for i in range(500):
        fn = fake.first_name()
        last_name = fake.last_name()
        salary = fake.random_element(elements=(100000, 125000, 200000, 50000, 75000))
        email = fake.email()
        company = fake.random_element(elements=("SpaceX", "Google", "Microsoft", "IBM", "OpenAI", "NASA"))
        job = fake.random_element(elements=("Programmer", "Manager", "CEO", "Tester", "TeamLead", "DB Admin", "Software Engineer"))
        location = fake.random_element(elements=("Hyderabad", "Bangalore", "Somalia", "Mumbai", "Mogadishu", "Delhi"))
        address = fake.address()

        SoftwareDeveloper(
            first_name=fn,
            last_name=last_name,
            salary=salary,
            email=email,
            company=company,
            job=job,
            location=location,
            address=address
        ).save()

    return HttpResponse("Successfully inserted 500 records into the SoftwareDeveloper table.")

def programmerspage(request):
    data = SoftwareDeveloper.objects.all() 
    my_dict = {"Programmers":data}
    return render(request, 'programmerswebpage.html', context=my_dict)


def somalia_data(request): 
    

    if request.method == "POST":
        cmp = request.POST.get('company')
        data = SoftwareDeveloper.objects.filter(location="Somalia") & SoftwareDeveloper.objects.filter(company=cmp)
        my_dict = {"Programmers":data}

    else:
        data = SoftwareDeveloper.objects.filter(location="Somalia") 
        my_dict = {"Programmers":data} 

   
    return render(request, 'somalia_data.html',context=my_dict)

def mogadisu_data(request): 
    if request.method == "POST":
        cmp = request.POST.get('company')
        data = SoftwareDeveloper.objects.filter(location="Mogadishu") & SoftwareDeveloper.objects.filter(company=cmp)
        my_dict = {"Programmers":data}
    else:
        data = SoftwareDeveloper.objects.filter(location="Mogadishu") 
        my_dict = {"Programmers":data}    
    return render(request, 'mogadisu_data.html',context=my_dict)


def hyderabad_data(request): 
    if request.method == "POST":
        cmp = request.POST.get('company')
        data = SoftwareDeveloper.objects.filter(location="Hyderabad") & SoftwareDeveloper.objects.filter(company=cmp)
        my_dict = {"Programmers":data}
    else:
        data = SoftwareDeveloper.objects.filter(location="Hyderabad") 
        my_dict = {"Programmers":data}    
    return render(request, 'hyderabad_data.html',context=my_dict)

def mumbai_data(request): 
    if request.method == "POST":
        cmp = request.POST.get('company')
        data = SoftwareDeveloper.objects.filter(location="Mumbai") & SoftwareDeveloper.objects.filter(company=cmp)
        my_dict = {"Programmers":data}
    else:
        data = SoftwareDeveloper.objects.filter(location="Mumbai") 
        my_dict = {"Programmers":data}    
    return render(request, 'mubai_data.html',context=my_dict)

  

