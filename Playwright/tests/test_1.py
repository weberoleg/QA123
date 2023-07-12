import requests
import json
from config import *

def test_get_users(get_users):
    assert get_users.status_code == 200
    req = get_users.json()
    assert(req['data'][0]['last_name']) == 'Lawson'
   

def test_get_user():
    r = requests.get(url_get_user)
    assert r.status_code == 200
    req = r.json()
    assert(req['data']['first_name']) == 'Janet'



def test_singl_user():
    r = requests.get('https://reqres.in/api/users/23')
    assert r.status_code == 404
    req = r.json()
    assert not req

def test_list_unknown():
    r = requests.get('https://reqres.in/api/unknown')
    assert r.status_code == 200
    req = r.json()
    assert (req['data'][2]['name']) == 'true red'

def test_singl_resourse():
    r = requests.get('https://reqres.in/api/unknown/23')
    assert r.status_code == 404, 'Error: wrong status code'
    req = r.json()
    assert not req


def test_post_user():
    r = requests.post(url=url_create_user,data =params_create_user)
    assert r.status_code == 201