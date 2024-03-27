from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST, require_GET
from study_hub.models import Publication


# Debug False
def handler404(request, exception):
    custom_message = "¡Oops! Parece que te has perdido."

    return render(
        request,
        "404.html",
        {"title": "Error 404", "exception": exception, "custom_message": custom_message},
        status=404,
    )


@require_GET
def home(request):

    return render(request, "home.html", {"title": "Maidana App"})


@require_POST
def searchNavbar(request):
    query = request.POST.get("query", "")
    if len(query) < 2:
        return JsonResponse({"publications": []})

    results_title = Publication.objects.filter(title__icontains=query)
    result_list = [
        {
            "title": str(item.title),
            "subject": str(item.subject),
            "id": item.id,
            "subject_id": item.subject_id,
        }
        for item in results_title
    ]

    return JsonResponse({"publications": result_list})


@require_GET
def about_me(request):

    return render(request, "about.html", {"title": "Acerca de Mí"})
