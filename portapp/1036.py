#
# settings.py
#

# I use this in the 'upload_to' arg for FileFields
# and ImageFields, hence making it a setting.
UPLOAD_PATH = 'uploads/%Y/%m'


#
# this can go wherever (mine is just at the top of my views.py)
#

from django.conf import settings

from datetime import date
import os

def handle_uploads(request, keys):
    saved = []

    upload_dir = date.today().strftime(settings.UPLOAD_PATH)
    upload_full_path = os.path.join(settings.MEDIA_ROOT, upload_dir)

    if not os.path.exists(upload_full_path):
        os.makedirs(upload_full_path)

    for key in keys:
        if key in request.FILES:
            upload = request.FILES[key]
            while os.path.exists(os.path.join(upload_full_path, upload.name)):
                upload.name = '_' + upload.name
            dest = open(os.path.join(upload_full_path, upload.name), 'wb')
            for chunk in upload.chunks():
                dest.write(chunk)
            dest.close()
            saved.append((key, os.path.join(upload_dir, upload.name)))
    # returns [(key1, path1), (key2, path2), ...]
    return saved


#
# example usage in a view
#

def my_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST, request.FILES)
        if form.is_valid():
            my_instance = MyModel()
            ...

            saved_images = handle_uploads(request, ['thumbnail_image', 'banner_image'])
            for image in saved_images:
                setattr(my_instance, image[0], image[1])

            my_instance.save()

            ...
