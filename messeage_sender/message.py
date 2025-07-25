#WhatsApptan otomatik mesaj gönderme/send automatic messages from WhatsApp
import pywhatkit as kit
phone_number = "+90" #mesajı göndermek istediğiniz kişinin numarası/the phone number of the person you want to leave a message
message="i love you" #mesaj/message
#göndermek istediğin zaman/the time you want to send
hour=15
minute=6
kit.sendwhatmsg(phone_number,message,hour,minute)