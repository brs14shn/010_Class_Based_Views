from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import StudentForm
from .models import Student
# Create your views here.
from django.views.generic import TemplateView, ListView, DetailView

# ?====FUNCTİON BASED==========================


def home(request):
    return render(request, "fscohort/home.html")

#!======= CLASS BASED=========================


class HomeView(TemplateView):
    template_name = "fscohort/home.html"

# ?====FUNCTİON BASED==========================


def student_list(request):
    students = Student.objects.all()
    context = {
        "students": students
    }
    return render(request, "fscohort/student_list.html", context)


#!======= CLASS BASED=========================
class StudentListView(ListView):
    model = Student
    context_object_name = "students"
    paginate_by = 1


def student_add(request):
    form = StudentForm()

    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("list")

    context = {

        "form": form
    }

    return render(request, "fscohort/student_add.html", context)


def student_detail(request, id):
    student = Student.objects.get(id=id)
    context = {
        "student": student
    }

    return render(request, "fscohort/student_detail.html", context)


class StudentDetailView(DetailView):
    model = Student
    pk_url_kwarg = 'id'
    # Default pk olarak url kısmında belirtirsek burada belirtmeye gerek yok


def student_update(request, id):

    student = Student.objects.get(id=id)

    form = StudentForm(instance=student)

    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect("list")

    context = {

        "student": student,
        "form": form
    }

    return render(request, "fscohort/student_update.html", context)


def student_delete(request, id):

    student = Student.objects.get(id=id)

    if request.method == "POST":

        student.delete()
        return redirect("list")

    context = {
        "student": student
    }
    return render(request, "fscohort/student_delete.html", context)
