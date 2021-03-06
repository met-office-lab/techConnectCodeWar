from urllib import request
import json

def __api(path, method=None):
    base_url = 'http://52.30.71.22:3000/conn4/api/'
    response = request.urlopen(request.Request(base_url + path, method=method))
    return json.load(response)


def state():
    data = []
    data = __api('state').splitlines()
    for i, row in enumerate(data):
        data[i] = row.strip()
    return data

def print_state():
    data = []
    data = __api('state').splitlines()
    for i, row in enumerate(data):
        data[i] = row.strip()
        print(data[i])
    return None

def play(player, col):
    player = player.upper()
    assert player == 'X' or player == 'O'
    assert 0 <= col <= 6
    assert isinstance(col, int)
    return __api('play/' + player + '/' + str(col), method="PUT")

def restart():
    return __api('reset', method='PUT')

if __name__ == "__main__":
    print(restart())
    print(state())
    print(play('X', 1))
    print(state())
    print(play('O', 1))
    print(play('X', 0))
    print(state())
    print(restart())
    print(state())
