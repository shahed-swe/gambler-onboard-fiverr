from django.http import JsonResponse


def bad_request():
    return JsonResponse({'error': 'Bad request'}, status=400)


def error_request(error, error_field=None, status=400):
    data = {'error': error}
    if error_field is not None:
        data['error_field'] = error_field
    return JsonResponse(data, status=status)
