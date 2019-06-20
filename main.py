from geopy.geocoders import Nominatim
import csv
import time


def comparison(received_value, reference_value):
    if not received_value == reference_value:
        print('Данные не совпадают, \n' + received_value + ' != ' + reference_value)
        return False
    else:
        return True


def get_input_data(csv_path):
    input_data = []
    with open(csv_path, "r") as csv_path:
        reader = csv.reader(csv_path, delimiter=';')
        for row in reader:
            input_data.append(row)
    return input_data


def test_address(file_name):
    data = get_input_data(file_name)
    geolocator = Nominatim(user_agent="specify_your_app_name_here")
    for line in data:
        time.sleep(1)
        location = geolocator.geocode(line[0])
        latitude = str(location.latitude)
        longitude = str(location.longitude)
        if comparison(latitude + '  ' + longitude, line[1]):
            return True
        else:
            return False


def test_coordinates(file_name):
    data = get_input_data(file_name)
    geolocator = Nominatim(user_agent="specify_your_app_name_here")
    for line in data:
        time.sleep(1)
        location = geolocator.reverse(line[1])
        address = location.address
        if comparison(address, line[0]):
            return True
        else:
            return False


if __name__ == "__main__":
    if test_coordinates('input_data_coordinates.csv') and test_address('input_data_address.csv'):
        print('Тесты успешной пройдены!')
        exit(0)
    else:
        print('Тесты не пройдены')
        exit(1)
