import requests
from datetime import timedelta, datetime





headers = {
    'Content-Type': 'application/json' ,
    'Authorization': 'Basic MTEzMTM6MVd5OW9tY2ZXNmppYXYycVpYdU1IaQ==',
}


date1 = datetime.now()



def cascade(parent= None, phone= None, text= None, textMessager= None ):
    data = ('[{"destination":"'+phone+'","localSendTime":"'+str(date1)[:19]+'","localCompletionTime":"'+str(date1+timedelta(hours=9))[:19]+'","useLocalTime":true,"hours":[10,11,12,13,14,15,16,17,18,19,20],"days":[1,2,3,4,5,6,7],"shortUrl":true,"callbackUrl":"https://domain.com/callback","callbackEvents":["delivered","price","click"],"cascade":[{"channelType":"VK","senderName":"idgtl_infonix_vk","content":{"text":"'+textMessager+'"},"condition":"not_read","ttl":14000},{"channelType":"TELEGRAM","senderName":"infonix_fatezh_bot","content":{"contentType":"text","text":"'+textMessager+'"},"condition":"not_delivered","ttl":600},{"channelType":"SMS","senderName":"sms_promo","content":{"text":"'+text+'"}}]}]').encode()
    #data = ('[{"destination":"'+phone+'","localSendTime":"'+str(date1)[:19]+'","localCompletionTime":"'+str(date1+timedelta(hours=9))[:19]+'","useLocalTime":true,"hours":[10,11,12,13,14,15,16,17,18,19,20],"days":[1,2,3,4,5,6,7],"shortUrl":true,"callbackUrl":"https://domain.com/callback","callbackEvents":["delivered","price","click"],"cascade":[{"channelType":"TELEGRAM","senderName":"infonix_fatezh_bot","content":{"contentType":"text","text":"текст сообщения"},"condition":"not_delivered","ttl":600},{"channelType":"VK","senderName":"idgtl_infonix_vk","content":{"text":"Ваш заказ готов к выдаче, Инфоникс Фатеж Пн-Пт 10-17,Сб 10-15 Сумма:"},"condition":"not_read","ttl":14400},{"channelType":"SMS","senderName":"sms_promo","content":{"text":"текст сообщения"}}]}]').encode()
    response = requests.post('https://direct.i-dgtl.ru/api/v1/message/cascade', headers=headers, data=data)
  
    if ('200' in str(response)):
        print ('OK')
        return "OK"
    else:
        return "error"+str(response)
#    print (response.text)
#    print (response)

#cascade(None,'9192109773')