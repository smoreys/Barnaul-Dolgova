import math
def find_spn(json_response):
    one = json_response['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['boundedBy']['Envelope']
    low = list(map(float, one['lowerCorner'].split()))  # координаты верхнего и нижнего углов объекта на сетке
    up = list(map(float, one['upperCorner'].split()))
    a, b = str(math.fabs(low[0] - up[0])), str(math.fabs(low[1] - up[1]))
    return a, b