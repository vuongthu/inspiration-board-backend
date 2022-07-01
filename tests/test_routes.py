import pytest
from app.models.board import Board
from app.models.card import Card


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