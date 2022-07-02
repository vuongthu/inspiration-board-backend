from urllib import response
import pytest
from app.models.board import Board
from app.models.card import Card


#GET/boards
def test_get_no_saved_boards(client):
    response = client.get("/boards")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == []



#GET/boards
def test_get_boards(client, one_board):
    response = client.get("/boards")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == [{
            "id" : 1,
            "title": "Motivational Quotes",
            "owner": "Nostalgia"
    }]


#GET/boards/1/cards
def test_get_cards_no_saved_cards(client, one_board):
    response = client.get("/boards/1/cards")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == []


#GET/boards/1/cards
def test_get_cards_by_board_id(client, one_card):
    response = client.get("/boards/1/cards")
    response_body = response.get_json()

    assert response.status_code == 200
    assert  response_body == [{
            "id" : 1,
            "likes_count" : 0,
            "message": "Motivation is what gets you started. Habit is what keeps you going"
    }]


#GET/boards/1/cards
def test_get_cards_when_no_board_id(client):
    response = client.get("/boards/1/cards")
    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body == {
    "details" : "No Board data with id: 1"   
    }


#DELETE /boards/1
def test_delete_board(client, one_board):
    response = client.delete("/boards/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert "details" in response_body
    assert response_body == {"details": "Board #1 successfully deleted"}
    assert Board.query.get(1) == None


def test_delete_board_not_found(client):
    response = client.delete("/boards/1")
    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body == {"details": "No Board data with id: 1"}