# API

# URL_SERVICE хранит базовый URL веб-сервиса, который используется для доступа к API или другим ресурсам.

URL_SERVICE = "https://2805c6fd-eff4-4bf8-bb98-a65f63baf51a.serverhub.praktikum-services.ru"

CREATE_ORDER = "/api/v1/orders"

# CREATE_ORDER хранит путь к API-методу для создания нового заказа.
# Этот путь будет использоваться для формирования полного URL-адреса в сочетании с базовым URL сервиса,
# когда необходимо выполнить запрос на создание заказа.
GET_ORDER_BY_TRACK = "/api/v1/orders/track"

#GET_ORDER_BY_TRACK хранит путь к API-методу для получения данных о заказе по трек-номеру