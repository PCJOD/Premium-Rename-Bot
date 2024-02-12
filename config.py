import re, os, time

id_pattern = re.compile(r'^.\d+$') 

class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "27397677") #⚠️ Required
    API_HASH  = os.environ.get("API_HASH", "808e9452b5d8b6ca9fe7ff6f6ee60fec") #⚠️ Required
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6883869171:AAFHmz6FOBnHmyBKJFQTQcyavLr3WyfbWOE") #⚠️ Required
    
    #premium client
    STRING = os.environ.get("STRING", "BQGiDi0ApKWE1pDgG2lQfOvtTcHnkk4zAqoL8Uqhm-65G7KyOniWjbD-ATM3uoOYgKOi48oIRjCwnSWYk3yqksUuMPOU6Bt5lAUC6KFJemokA0K6qhT7s-8nAB80PGD8yML_u_yGDMxsniUpxKJnst_Luu4l3gQbUUnidO_twW9oIC9hQRD0JXrGK2uK7lqea5K7qnYXsqT16c3no2opFhzeXnBjklr9Sxz2TrbNH_G3Bi4d8Y3W8mqgNdbWlDXfMZuLc6HTjpgs2iZG1pMsEeHCgQHctKOaKwYmARq9tyGKOcM0Y6VviKj6xUUfGgcgWYK39VozcRyjgaZz9Phh4DBrixNIkAAAAAFgOLaZAA") #⚠️ Required 
    STRING_API_ID = os.environ.get("STRING_API_ID", "true") # ⚠️ Required
    STRING_API_HASH = os.environ.get("STRING_API_HASH", "true") # ⚠️ Required
   
    # database config
    DB_NAME = os.environ.get("DB_NAME","Cluster0")     
    DB_URL  = os.environ.get("DB_URL","mongodb+srv://Cluster0:Cluster0@cluster0.2erkpzk.mongodb.net/?retryWrites=true&w=majority") #⚠️ Required
 
    # other configs
    BOT_UPTIME  = time.time()
    ADMIN       = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '-1002113853127').split()] #⚠️ Required
    FORCE_SUB   = os.environ.get("FORCE_SUB", "pcott") #⚠️ Required Username without @
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002113853127")) #⚠️ Required
    FLOOD = int(os.environ.get("FLOOD", '10'))
    BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    PORT = int(os.environ.get("PORT", "8080"))
