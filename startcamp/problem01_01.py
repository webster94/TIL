import json


def kfood(restaurant):
    pass


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    restaurant_json = open('problem01_data.json', encoding='UTF8')
    restaurant = json.load(restaurant_json)
    print(kfood(restaurant)) 
    # => True