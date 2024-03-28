from rest_framework.decorators import api_view
from rest_framework.response import Response
from img_to_text.models import Img2Text
from img_to_text.utils import upload_img_firebase
from rest_framework.decorators import api_view
import requests


@api_view(['POST'])
def extract_text_from_image(request):
    if request.method == 'POST':
        # OCR.space API endpoint
        api_url = 'https://api.ocr.space/parse/image'
        api_key = 'a1b0cf195288957'

        payload = {
            'apikey': api_key,
            'language': 'ara',  # Language code for Arabic
        }

        # Get the image file from the request
        image_file = request.FILES.get('image')

        if image_file:
            image_file.seek(0)
            # Send POST request to OCR.space API
            response = requests.post(api_url, files={'image': image_file}, data=payload)

            # Parse response JSON
            result = response.json()
            # Extract text from the response
            if 'ParsedResults' in result and len(result['ParsedResults']) > 0:
                extracted_text = result['ParsedResults'][0]['ParsedText']
                image_url = upload_img_firebase(image_file)
                Img2Text.objects.create(image=image_url, extracted_text=extracted_text)
                return Response({'text': extracted_text})
            else:
                return Response({'error': 'No text extracted'}, status=400)
        else:
            return Response({'error': 'Empty image file'}, status=400)

    return Response({'error': 'Invalid request'}, status=400)
from twilio.rest import Client
