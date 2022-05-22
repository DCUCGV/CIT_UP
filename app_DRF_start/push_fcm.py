import django
django.setup()
# import app_DRF_start
from app_DRF_start.models import Info
# from app_DRF_start.models import Info
from firebase_admin import messaging
from datetime import datetime
from celery import shared_task

# from pyfcm import FCMNotification
@shared_task
def send_to_firebase_cloud_messaging():
    # This registration token comes from the client FCM SDKs.
    # registration_token = 'fiehr6lMTVCZke1wyMDvEO:APA91bE3B4P-FYgodbHUAnzmCfcsK_V022Ud0t9eMg9-SJTkFj90q-RAWtgpwNJPzlO9hAMA2yEpw79Y6SXQg-fcAIqaWpF0GiC_mQlX6-R0R4JWekzcJFUUneiyc8kA778xNuI79lyf'
    registration_token = 'd7RcxUFdSmaUG13TCMFbkf:APA91bFhn_ri0r4ZtDU1TYjwO-qaECC7FzwcCYcdEBAuF4jhd64F3TAEemwVVsYXwEfIJV3MXN1sDpU1dKmNuu2y6BueS3PuTW67ITansUkXMwrRy572XrYEOJkvAFglQh17swsCi_ex'
    # See documentation on defining a message payload.
    print("=============================")
    print("volume : ",end="")
    # a = Info.objects.values('volume')
    # test = a.
    volume = Info.objects.last().volume
    print(volume)
    if volume >= 80.00 :
        message = messaging.Message(

            notification=messaging.Notification(
            title='압축 안내',
            body='현재 포화도는 '+str(volume)+'% 입니다.\n'+'압축을 진행합니다.',
            ),
        token=registration_token,
        )
    # print(datetime.now())
    # return



    # response = messaging.send(message)
    # Response is a message ID string.
    # print('Successfully sent message:', response)
    try:
        response = messaging.send(message)
        print('Successfully sent message:', response)

    except Exception as e:
        print('예외발생')