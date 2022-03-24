from lib2to3.pytree import Base
from urllib import response
import requests

BASE="http://127.0.0.1:5000/"

import pytest

@pytest.fixture
def bookdata():
    return {
        '1':{'authorname': 'Micheal J. Bob', 'name': 'ALmond Tree'},
        '2':{'authorname': 'Khaled HUssaini','name': 'Kite Runner'},
        '3':{'authorname': 'Mohsin Hamid', 'name': 'Exit West'},
    }

@pytest.mark.parametrize("book_id,output", [
    ('1', {'id':1,'authorname': 'Micheal J. Bob',  'name': 'ALmond Tree'}),
    ('2', {'id':2,'authorname': 'Khaled HUssaini', 'name': 'Kite Runner'}),
    ('3', {'id':3,'authorname': 'Mohsin Hamid', 'name': 'Exit West'}),
])
def test_put_book_data(book_id,bookdata,output):
    response=requests.put(BASE + "books/"+str(book_id), bookdata[book_id])
    assert response.json() == output

@pytest.mark.parametrize("book_id,output", [
    ('3', {'id':3, 'authorname': 'Mohsin Hamid', 'name': 'Exit West'}),
])
def test_patch_book_data(book_id,output):
    response=requests.patch(BASE + "books/"+str(book_id),{'authorname': 'Mohsin Hamid'})
    assert response.json() == output

@pytest.mark.parametrize("book_id,output", [
    ('1', {'id':1,'authorname': 'Micheal J. Bob',  'name': 'ALmond Tree'}),
    ('2', {'id':2,'authorname': 'Khaled HUssaini', 'name': 'Kite Runner'}),
    ('3', {'id':3,'authorname': 'Mohsin Hamid', 'name': 'Exit West'}),
])
def test_get_book_data(book_id,output):
    response=requests.get(BASE + "books/"+str(book_id))
    assert response.json() == output

@pytest.mark.parametrize("book_id, output", [
    ('1', 204),
    ('2', 204),
    ('3', 204),
])
def test_delete_book_data(book_id, output):
    response=requests.delete(BASE + "books/"+str(book_id))
    assert response.status_code == output

def test_delete_book_data_if_not_exist():
    response=requests.delete(BASE + "books/"+str(5))
    assert response.status_code == 404
    assert response.json() == {'message':'Could not delete as no book exist with that id'}

