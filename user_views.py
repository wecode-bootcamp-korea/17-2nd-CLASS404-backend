# user/views

import requests

from class404.utils import s3_handler

class MyPageImageUploadView(View):
    @login_decorator
    def post(self, request):
        file = request.FILES.get('fileName')
        user = request.user

        if not file:
            return JsonResponse(
                {"message": "IMAGE_DOES_NOT_EXIST"},
                status=400
                )
        
        user.image_url = s3_handler(file)
        user.save()
        return JsonResponse(
            {"file_url": user.image_url},
            status=200
            )