from datetime import datetime

class userInfo:
    def __init__(self, email:str, name:str):
        self.email = email
        self.name = name
        self.created_at: str = datetime.now().strftime("%d/%m/%Y")

    def get(self) -> dict:
        return {
            "email": self.email,
            "name": self.name,
            "created_at": self.created_at
        }
    
class userLog:
    def __init__(self, email:str, start_date:str, price:float, end_date:str|None, product_name:str, date_diff:int|None):
        self.email = email
        self.start_date = start_date
        self.price = price
        self.end_date = end_date
        self.product_name = product_name
        self.date_diff = date_diff

    def get(self) -> dict:
        return {
            "email": self.email,
            "start_date": self.start_date,
            "price": self.price,
            "end_date": self.end_date,
            "product_name": self.product_name,
            "date_diff": self.date_diff
        }