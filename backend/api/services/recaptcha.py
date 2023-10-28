import requests
from django.conf import settings
from backend.api import helpers


def check_recaptcha_token(recaptcha_token):
    if not settings.GOOGLE_RECAPTCHA_ENABLED:
        return True

    post_data = {
        'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
        'response': recaptcha_token
    }

    verify_response = requests.post('https://www.google.com/recaptcha/api/siteverify', data=post_data).json()
    print(verify_response)

    if not verify_response['success']:
        return helpers.error_request('Captcha is invalid', 'recaptcha_token')
    else:
        return None
