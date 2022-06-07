import django
django.setup()

from app_DRF_start.models import Info
from firebase_admin import messaging
from celery import shared_task

@shared_task
def send_to_firebase_cloud_messaging():
    # This registration token comes from the client FCM SDKs.
    registration_token = 'fiehr6lMTVCZke1wyMDvEO:APA91bE3B4P-FYgodbHUAnzmCfcsK_V022Ud0t9eMg9-SJTkFj90q-RAWtgpwNJPzlO9hAMA2yEpw79Y6SXQg-fcAIqaWpF0GiC_mQlX6-R0R4JWekzcJFUUneiyc8kA778xNuI79lyf'
    # registration_token = 'eZDPrI7hRMu8LTMuikSFWu:APA91bFx6nZBG34i8qC2EvAAWzwgKnPw_8nTDK6DPjeiOz9oRA5kDaEXyQaHmH603_M7v9lbEKcYl17s0p9Pa0pBC2mYWYh-23RdFRlI5L5UGvK-svfFh77TmjGUJvcV--qED1fOHIj2'
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