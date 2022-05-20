from firebase_admin import messaging
# from pyfcm import FCMNotification
def send_to_firebase_cloud_messaging():
    # This registration token comes from the client FCM SDKs.
    # registration_token = 'fiehr6lMTVCZke1wyMDvEO:APA91bE3B4P-FYgodbHUAnzmCfcsK_V022Ud0t9eMg9-SJTkFj90q-RAWtgpwNJPzlO9hAMA2yEpw79Y6SXQg-fcAIqaWpF0GiC_mQlX6-R0R4JWekzcJFUUneiyc8kA778xNuI79lyf'
    registration_token = 'd7RcxUFdSmaUG13TCMFbkf:APA91bFhn_ri0r4ZtDU1TYjwO-qaECC7FzwcCYcdEBAuF4jhd64F3TAEemwVVsYXwEfIJV3MXN1sDpU1dKmNuu2y6BueS3PuTW67ITansUkXMwrRy572XrYEOJkvAFglQh17swsCi_ex'
    # See documentation on defining a message payload.
    message = messaging.Message(

        notification=messaging.Notification(
            title='안녕하세요 타이틀 입니다',
            body='안녕하세요 메세지 입니다',
        ),
        token=registration_token,
    )

    # response = messaging.send(message)
    # Response is a message ID string.
    # print('Successfully sent message:', response)
    try:
        response = messaging.send(message)
        print('Successfully sent message:',response)
    except Exception as e:
        print('예외발생')

# from pyfcm import FCMNotification
#
# APIKEY = "AAAAse8vjbM:APA91bGC8GSWo8miWRQ_QeyIrkJNKtPqptXw1gFvkZYN35I5cdTylK4F_v9zEsKdEZvHTAMuuU5Bvc6HpVfA3jgdOSQ3PryKQ32oSbDtqYCPzprJSnlAlmCWqyw2lCG2f7njd1kB_fo8"
# TOKEN = "fxzSOHu_SjCo6gnbFlJm9L:APA91bFtyF2QKpGy91-V_UDpwu19LSeEET2hOb3PHvCnROyD0OGY4MbzpAcWn8qhqEYspUZWM-Wdr-vFrPXjd04PXaaFwPQTKyxV48DLSTVxG742br33p-OCcq4IYvawoMvXc2KnwiF3"
#
# push_service = FCMNotification(APIKEY)
# def sendMessage(body, title):
#     data_message={
#         "body":body,
#         "title":title
#     }
#
#     result = push_service.single_device_data_message(registration_id=TOKEN, data_message=data_message)
#
#     print(result)
