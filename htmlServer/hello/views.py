from django.http import HttpResponse
import os
module_dir = os.path.dirname(__file__)
file_path = os.path.join(module_dir, "obama.jpg")
def index(request):
    module_dir = os.path.dirname(__file__)
    file_path = os.path.join(module_dir, "obama.jpg")
    with open(file_path, "rb") as f:
        return HttpResponse(f.read(), content_type="image/jpg")
    #return HttpResponse("This is dumb. I can't beleive spring boot is more elegent than this shit")