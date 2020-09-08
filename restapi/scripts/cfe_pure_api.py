import requests
import json

BASE_URL = "http://127.0.0.1:8000/"

ENDPOINT = "api/updates/"


def get_list():

    r = requests.get(BASE_URL + ENDPOINT)

    print(r.status_code)

    if r.status_code != '404':

        print("yeppppppi")

    data = r.json()

    for obj in data:

        if obj['pk'] == 1:
            r = requests.get(BASE_URL + ENDPOINT + str(obj['pk']))

            print(r.json())

    return data


get_list()


def create_update():

    dict_ = {'user': 1, "content": 'another new update'}

    r = requests.delete(BASE_URL + ENDPOINT, data=dict_)

    # r = requests.post(BASE_URL + ENDPOINT, data=dict_)

    if r.status_code == requests.codes.ok:

        return r.json()

    return r.text


create_update()
