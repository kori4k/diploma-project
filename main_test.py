import configuration
import sender_stand_request
import data

# Проверить что запрос на получение инфо по треку - 200
def test_receive_info():
    info_response = sender_stand_request.get_info()
    assert info_response.status_code == 200