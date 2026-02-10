from sender_stand_request import create_order, get_order_by_track


def test_create_order_and_get_by_track():
    # Создать заказ
    order_body = {
        "firstName": "Ivan",
        "lastName": "Ivanov",
        "address": "Moscow",
        "metroStation": 1,
        "phone": "+79999999999",
        "rentTime": 3,
        "deliveryDate": "2026-02-09",
        "comment": "Test order",
        "color": ["BLACK"]
    }

    create_response = create_order(order_body)

    # Проверка: заказ создан
    assert create_response.status_code == 201

    # Шаг 2. Сохранить трек
    track = create_response.json()["track"]

    # Шаг 3. Получить заказ по треку
    get_response = get_order_by_track(track)

    # Шаг 4. Проверить код ответа
    assert get_response.status_code == 200

