from sender_stand_request import create_order, get_order_by_track
from data import order_body


def test_create_order_and_get_a_track():
    # Создать заказ

    create_response = create_order(order_body)
    # Заказ создан
    assert create_response.status_code == 201
    assert "track" in create_response.json()
   
def test_get_order_by_track():
    # Объявление тестовой функции.
    create_response = create_order(order_body)
    # вызов функции, которая делает POST-запрос к API
    track = create_response.json()["track"]
    # сохранить в переменную track номер заказа
    get_response = get_order_by_track(track)
    # вызвать функцию получения заказа, объявляем переменную get_response
    assert get_response.status_code == 200
    # проверка, что сервер вернул статус 200 (OK)

# Елизавета Савостьянова, 41-я(39) когорта — Финальный проект. Инженер по тестированию плюс