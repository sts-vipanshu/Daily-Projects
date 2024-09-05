from django.http import (
    HttpResponse,
    HttpResponsePermanentRedirect,
    HttpResponseRedirect,
)
from django.shortcuts import get_object_or_404, redirect, render

from .forms import StudentForm
from .models import StudentData


def listView(request) -> HttpResponse:
    context = {}
    context["students"] = StudentData.objects.all()
    return render(request=request, template_name="listView.html", context=context)


def createView(
    request,
) -> HttpResponseRedirect | HttpResponsePermanentRedirect | HttpResponse:
    if request.method == "POST":
        form = StudentForm(data=request.POST or None)
        if form.is_valid():
            form.save()
            return redirect(to="listView")
    else:
        form = StudentForm()
    return render(
        request=request, template_name="createView.html", context={"form": form}
    )


def updateView(
    request, student_id
) -> HttpResponseRedirect | HttpResponsePermanentRedirect | HttpResponse:
    student = get_object_or_404(klass=StudentData, student_id=student_id)
    form = StudentForm(data=request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect(to="listView")
    return render(
        request=request, template_name="createView.html", context={"form": form}
    )


def deleteView(
    request, student_id
) -> HttpResponseRedirect | HttpResponsePermanentRedirect:
    student = StudentData.objects.get(student_id=student_id)
    student.delete()
    return redirect("listView")
