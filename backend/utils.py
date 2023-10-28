import os
import re
import secrets
import collections.abc
from io import BytesIO

from django.contrib.auth.models import AnonymousUser


email_re = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
username_re = re.compile('[a-zA-Z0-9_]{3,16}')
password_re = re.compile('^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$')
zip_code_re = re.compile('[a-z0-9][a-z0-9\\- ]{0,10}[a-z0-9]')
two_step_code_re = re.compile('[0-9]{6,8}')


def is_valid_email(email):
    return email_re.match(email)


def is_valid_username(email):
    return username_re.match(email)


def is_valid_password(password):
    return password_re.match(password)


def is_valid_zip_code(zip_code):
    return zip_code_re.match(zip_code)


def is_valid_two_step_code(code):
    return two_step_code_re.match(code)


def make_random_string(length=10, allowed_chars='abcdefghjkmnpqrstuvwxyz'
                                                'ABCDEFGHJKLMNPQRSTUVWXYZ'
                                                '23456789'):
    return ''.join(secrets.choice(allowed_chars) for i in range(length))


def clip_text(string, max_length):
    if len(string) > max_length:
        return string[0:max_length]

    return string


def pluralize(number, text):
    if number == 1:
        return text
    else:
        return text + "s"


def compute_usernames(user, usernames):
    in_view = []

    if not isinstance(user, AnonymousUser):
        if user.username in usernames:
            in_view.append(user.username)

    for username in usernames:
        if username in in_view:
            continue

        in_view.append(username)
        if len(in_view) >= 3:
            break

    if len(usernames) > 3:
        in_view.append((usernames - 3).__str__())

    return in_view


def get_file_size(value):
    if hasattr(value, 'file'):
        if isinstance(value.file, BytesIO):
            return value.file.getbuffer().nbytes
        else:
            if hasattr(value.file, 'size'):
                return value.file.size
            elif os.path.exists(value.file.name):
                return os.path.getsize(value.file.name)
            else:
                raise AttributeError("Unable to determine the file's size.")
    else:
        raise AttributeError("Unable to determine the file attributes.")


def format_file_size(size):
    power = 2 ** 10
    n = 0
    power_labels = {0: '', 1: 'K', 2: 'M', 3: 'G', 4: 'T'}
    while size > power:
        size /= power
        n += 1
    return size, power_labels[n] + 'B'


def update_dict(d, u):
    for k, v in u.items():
        if isinstance(v, collections.abc.Mapping):
            d[k] = update_dict(d.get(k, {}), v)
        else:
            d[k] = v
    return d
