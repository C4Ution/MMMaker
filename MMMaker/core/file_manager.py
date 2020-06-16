from misc import get_random_name, random_str
from conf import settings
import requests
from tenacity import retry, stop_after_attempt
import boto3
import os


# @retry  # retry forever
# @retry(stop=stop_after_attempt(3))
def downloader(file_urls):
    file_paths = []

    for url in file_urls:
        file_name = get_random_name('mp4')
        file_paths.append(file_name)
        request = requests.get(url, stream=True)
        if request.status_code == 200:
            with open(file_name, 'wb') as f:
                for chunk in request.iter_content(1024):
                    f.write(chunk)
    """
    :param file_urls: 사용자가 업로드한 동영상 파일 url 리스트
    :return: 다운받은 절대 경로 리스트
    """
    return file_paths


def uploader(file_path):
    """
    :param file_path: 업로드할 파일 절대 경로
    :return: 업로드한 url
    """
    with open(file_path, 'rb') as f:
        contents = f.read()

    s3 = boto3.resource(
        's3', aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
    )
    bucket = s3.Bucket('mmmaker')
    key_name = random_str() + '.mp4'
    bucket.put_object(Key=key_name, Body=contents)
    os.remove(file_path)

    url = settings.CUSTOM_DOMAIN + key_name
    return url
