# API

# URL_SERVICE хранит базовый URL веб-сервиса, который используется для доступа к API или другим ресурсам.

URL_SERVICE = "https://5c2ecc72-37c7-4edc-a6c8-fd69d84abed1.serverhub.praktikum-services.ru"

CREATE_ORDER = "/api/v1/orders"

# CREATE_ORDER хранит путь к API-методу для создания нового заказа.
# Этот путь будет использоваться для формирования полного URL-адреса в сочетании с базовым URL сервиса,
# когда необходимо выполнить запрос на создание заказа.
GET_ORDER_BY_TRACK = "/api/v1/orders/track"

#GET_ORDER_BY_TRACK хранит путь к API-методу для получения данных о заказе по трек-номеру