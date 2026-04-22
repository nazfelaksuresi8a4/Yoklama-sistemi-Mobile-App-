import requests as rq
import pyrebase

class Backend:
    def __init__(self):
        self.api_state = 0
        self.config = {
            'apiKey': "",
            'authDomain': "",
            'databaseURL': "",
            'projectId': "",
            'storageBucket': "",
            'messagingSenderId': "",
            'appId': "",
            'measurementId': ""
                        }
        
        try:
            self.firebase = pyrebase.initialize_app(self.config)
            self.auth = self.firebase.auth()
            self.api_state = 1
        
        except:
            self.api_state = 0

    def login(self,email,password):
        login_status = None
        sign_up_status = None

        if self.api_state == 1:
            try:
                login_status = self.auth.sign_in_with_email_and_password(email,
                                                                         password)
            except Exception as e0fx:
                dct = {}
                memory = {}

                for enum,msg in enumerate(str(e0fx).split('\n')):
                    try:
                        key,val = msg.split(':')
                        dct[key] = val
                    except:
                        memory[enum] = msg.split(':')
                
                print(dct)
                
                return ('not',dct,memory)

            if login_status:
                return ('ok',login_status)
            else:
                print(f'is None')
        
        else:
            if sign_up_status:
                return ('not',login_status)
            else:
                print(f'is None')


    def sign_up(self,email,password):
        if self.api_state == 1:
            sign_up_status = self.auth.create_user_with_email_and_password(email,
                                                                        password)

            return ('ok',sign_up_status)

        else:
            return (1,'API ile bağlantı kurulurken bir sorun meyedana geldi lütfen daha sonra tekrar deneyiniz')
