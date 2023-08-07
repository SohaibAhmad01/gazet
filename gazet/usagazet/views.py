# views.py
from django.shortcuts import render, redirect
from usagazet.models import *
from django.core.exceptions import ValidationError
import csv
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count


def import_csv(request):
    if request.method == 'POST' and request.FILES.get('csv_file'):
        csv_file = request.FILES['csv_file']
        if not csv_file.name.endswith('.csv'):
            return render(request, 'error.html', {'message': 'Invalid file format. Please upload a CSV file.'})
        try:
            csvreader = csv.DictReader(csv_file.read().decode('utf-8').splitlines())
            import pdb;pdb.set_trace();
            for row in csvreader:
                
                Gradutes.objects.create(
                    roll_no=row['reg_number'],
                    name=row['name'],
                    father_name=row['father_name'],
                    cnic=row['cnic'],
                    degree_title=row['degree_title'],
                    session_enrolment_date=row['enrollment_date'],
                    session_completion_date=row['complete_date'],
                    degree_no=row['degree_number'],
                    remark=row['remarks'],
                )
            return render(request, 'success.html', {'message': 'Data imported successfully'})
        except ValidationError as e:
            return render(request, 'error.html', {'message': f'Error in CSV data: {e}'})
    return render(request, 'upload_csv.html')


def Dashboard(request):
    return render(request, 'upload_csv.html')




def recordPage(request):
    serial_number = 1  # Initialize the serial number as a global variable
    array_session=["BACHELOR OF COMPUTER SCIENCE",
                   "BACHELOR OF SCIENCE IN COMPUTER SCIENCE",
                   "Bachelor of Business Administration",
                   "Bachelor of Commerce",
                   "Bachelor of Computer Science",
                   "Bachelor of Education",
                   "Bachelor of Science in Computer Science",
                   "Bachelor of Science in Information Technology",
                   "Bachelor of Science in Software Engineering",
                   "Bachelor of Technology (Civil)",
                   "Bachelor of Technology (Civil)",
                   "Bachelor of Technology (Electrical)",
                   "Bachelor of Technology (Hons.) in Civil",
                   "Bachelor of Technology (Hons.) in Electrical",
                   "Bachelor of Technology (Hons.) in Electronics",
                   "Bachelor of Technology (Hons.) in Mechanical",
                   "Bachelor of Technology (Mechanical)",
                   "Bachelor of Technology (Pass) in Civil",
                   "Bachelor of Technology (Pass) in Electrical",
                   "Bachelor of Technology (Pass) in Electronics",
                   "Bachelor of Technology (Pass) in Mechanical",
                   "MASTER OF ACCOUNTING",
                   "Master of Accounting",
                   "Master of Arts in Economics",
                   "Master of Arts in English",
                   "Master of Business Administration",
                   "Master of Business Administration (Executive)",
                   "Master of Commerce",
                   "Master of Computer Science",
                   "Master of Science in Computer Science",
                   "Master of Science in Information Technology",
                   "Master of Science in Management Sciences",
                   "Master of Science in Mathematics",
                   "Masters of Education"
                   ]
    stud = []
    for session in array_session:
        students=Gradutes.objects.filter(degree_title=session).order_by('id')

    # Apply pagination for each query, with 12 results per page
        cs_students_paginator = Paginator(students, 12)
        page_num=cs_students_paginator.num_pages      
        for num in range(page_num): 
            cs_students = cs_students_paginator.get_page(num)
            stud.append(cs_students)
    print("degree_title", stud)
    
    
    
    return render(request, 'table.html',{
        "cs_students": stud,
        'std_count':Gradutes.objects.count(),
    })



def summaryPage(request):
    degrees_counts = Gradutes.objects.values('degree_title').annotate(count=Count('degree_title'))

    context = {
        'degrees_counts': degrees_counts,
    }
    
    return render(request,'summary.html', context)