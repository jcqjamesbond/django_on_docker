from django.http import JsonResponse
def echo(request):
    msg = request.GET.get("msg")
    result = {
        "msg": msg
    }
    return JsonResponse(result)
