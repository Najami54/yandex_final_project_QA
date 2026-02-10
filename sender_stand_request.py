import requests
from configuration import URL_SERVICE

def create_order(order_body: dict): #Создание заказа POST /api/v1/orders
       return requests.post(
        f"{URL_SERVICE}/api/v1/orders",
        json=order_body
    )


def get_order_by_track(track: int): #Получение заказа по треку GET /api/v1/orders/track?t=123456
       return requests.get(
        f"{URL_SERVICE}/api/v1/orders/track",
        params={"t": track}
    )
