from firebase_admin import storage
import datetime


def upload_img_firebase(image):
    bucket = storage.bucket()

    # Convert the datetime object to a timestamp (number of seconds since the epoch)
    timestamp_str = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")

    destination_blob_name = f"images/{timestamp_str}"
    image.seek(0)
    # Upload image to Firebase Storage
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_file(image)

    # Get the URL of the uploaded image
    url = blob.public_url
    return url

