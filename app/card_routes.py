from flask import Blueprint, request, jsonify, make_response
from app import db
from app.models.board import Board
from app.models.card import Card
from .routes_helper import success_msg, make_model, get_model_by_id

bp = Blueprint("cards_bp", __name__, url_prefix="/cards")


####  ROUTES  ####


#GET/cards
@bp.route("", methods=("GET",))
def get_all_boards():
    cards = Card.query.order_by("card_id").all()
    card_list = [card.to_dict() for card in cards]
    return jsonify(card_list), 200


#GET/card by id
@bp.route("/<card_id>/cards", methods=["POST"])
def create_card(card_id):
    request_body = request.get_json()
    new_card = make_model(Card, request_body, card_id=card_id)
    db.session.add(new_card)
    db.session.commit()
    return jsonify({"card": new_card.to_dict()}), 201


#PATCH/card
@bp.route("/<card_id>/like", methods=["PATCH"])
def update_like_card(card_id):

    card = get_model_by_id(Card, card_id)
    card.increase_likes()
    db.session.commit()
    return jsonify({"card": card.to_dict()}), 200


    # DELETE/card
@bp.route("<card_id>", methods=["DELETE"])
def delete_board (card_id):
    board = Board.query(card_id)
    db.session.delete(card_id)
    db.session.commit()
    return make_response(jsonify({"details": 'card successfully deleted'} ), 200)
