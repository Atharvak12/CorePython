
class InsufficientBalance(Exception):
    def __init__(self,balance =""):
        balance =""
        super().__init__("Not sufficient balance")