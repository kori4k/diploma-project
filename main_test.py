import configuration
import data
import requests

#создать новый заказ
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,  # подставляем полный url
                         json=body,  # тут тело
                         headers=data.headers)  # а здесь заголовки

#вернуть трек номер
def get_track_number():
    order = data.order_body.copy()
    new_order= post_new_order(order)
    return new_order.json()["track"]

#получить инфо по трек номеру
def get_info():
    return requests.get(configuration.URL_SERVICE + configuration.RECEIVE_ORDER + str(get_track_number()),
                         headers=data.headers)# а здесь заголовки


# Проверить что запрос на получение инфо по треку - 200
def test_receive_info():
    info_response = get_info()
    assert info_response.status_code == 200