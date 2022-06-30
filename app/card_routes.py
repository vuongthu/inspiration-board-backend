from flask import Blueprint, request, jsonify, make_response
from app import db
from app.models.board import Board
from app.models.card import Card
from .routes_helper import success_msg, make_model, get_model_by_id

bp = Blueprint("cards_bp", __name__, url_prefix="/cards")

#GET/card by id

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
