from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
import openpyxl

def index(request):
    return render(request, 'pages/index.html')

def upload(request):
    if request.method == 'GET':
        return render(request, 'pages/upload.html')
    else:
        new_questions = request.FILES['myfile']

        wb = openpyxl.load_workbook(new_questions)

        # getting a particular sheet by name out of many sheets
        worksheet = wb["Sheet1"]
        print(worksheet)

        excel_data = list()
        for row in worksheet.iter_rows():
            row_data = list()
            for cell in row:
                row_data.append(str(cell.value))
            excel_data.append(row_data)
        i = 0
        for data in excel_data[1:]:
            value = Question(
                i,
                data[0],
                data[1],
                data[2],
                data[3]
            )
            i=i+1
            if i>2:
                value.save()
        return HttpResponse("you have sucessfully uploaded data")

def list_data(request):
    data= Question.objects.all()
    cotext={
    "questions": data
        }
    return render(request,"pages/list.html", cotext)

def search(request):
        if request.method == "POST":
            query_list = Question.objects.all()
            keywords = request.POST["name"]
            if keywords:  # to check empty keyword
                    query_list = query_list.filter(
                        question__icontains=keywords
                    )
            return render(request, 'pages/search_result.html', {"results": query_list})

        return render(request, 'pages/list.html')