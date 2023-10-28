import os

from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions
from django.utils.deconstruct import deconstructible

from _io import BytesIO


@deconstructible
class ImageDimensionsValidator:
    min_width = 1
    min_height = 1

    def __init__(self, min_width=None, min_height=None):
        if min_width is not None:
            self.min_width = min_width

        if min_height is not None:
            self.min_height = min_height

    def __call__(self, value):
        image_width, image_height = get_image_dimensions(value.file)
        print(str(image_width) + ', ' + str(image_height))

        # if image_width < self.min_width or image_height < self.min_height:
            # raise ValidationError('Image doesn\'t meet dimensions requirements %dx%d (%dx%d)' % (self.min_width, self.min_height, image_width, image_height))

        pass


@deconstructible
class FileSizeValidator:
    limit = 1

    def __init__(self, limit=None):
        if limit is not None:
            self.limit = limit

    def __call__(self, value):
        if hasattr(value, 'file'):
            if isinstance(value.file, BytesIO):
                file_size = value.file.getbuffer().nbytes
            else:
                if hasattr(value.file, 'size'):
                    file_size = value.file.size
                elif os.path.exists(value.file.name):
                    file_size = os.path.getsize(value.file.name)
                else:
                    raise AttributeError("Unable to determine the file's size.")
        else:
            raise AttributeError("Unable to determine the file attributes.")

        if file_size > self.limit * 1024 * 1024:
            raise ValidationError('Max file size limit exceeded (%d MB)' % self.limit)
