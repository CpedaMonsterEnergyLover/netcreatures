import json

from Main.auth import only_authenticated
from rest_framework.views import APIView
from django.http import JsonResponse
from .models import WebsiteSignature, WebsiteType
from .parsing import WebsiteParser
from requests.exceptions import RequestException


class GetWebsiteSignature(APIView):
    @only_authenticated
    def post(self, request):
        data = json.loads(request.body)
        link = data.get('link')

        parser = WebsiteParser(link)
        domain = parser.extract_netloc()
        request_err = ""

        try:
            signature = WebsiteSignature.objects.get(domain=domain)

        except WebsiteSignature.DoesNotExist:
            signature = WebsiteSignature(domain=domain)

            try:
                extracted = parser.extract_text_from_url()[:2000]

                try:
                    suggested_type = parser.extract_type(extracted)
                    website_type = WebsiteType.objects.get(pk=suggested_type)
                    signature.type = website_type

                except WebsiteType.DoesNotExist:
                    pass

            except RequestException as e:
                signature.accessed = False
                request_err = e

            signature.save()

        return JsonResponse(data={
            'status': 'ok',
            'signature': signature.id,
            'request_err': request_err
        }, safe=False)
