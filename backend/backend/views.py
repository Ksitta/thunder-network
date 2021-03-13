from django.http import JsonResponse


def register(request):
    def responce(code: int, message: str):
        return JsonResponse(
            {
                'code': code,
                'message': message
            }
        )
    if request.method == 'POST':

        return responce(201, 'Success')
    else:
        return responce(405, 'Error')
