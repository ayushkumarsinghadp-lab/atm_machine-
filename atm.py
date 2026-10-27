class atm:
    def __init__(self):
        self.amount=10000
        self.pin=1234
    def card_insert(self):
        user_card=input('insert your card')
        if user_card=='card':
            print('card inserted')
        else:
            print('invaild card')
    def enter_pin(self):
        user_pin=int(input('enter the pin'))
        if user_pin==self.pin:
            print('pin correct')
            print('1)check balance\n2)withdraw')
            user

                