from flask import Blueprint, request, jsonify, make_response
from app import db
from app.models.board import Board
from app.models.card import Card
from .routes_helper import error_msg, success_msg, make_model, get_model_by_id

bp = Blueprint("boards_bp", __name__, url_prefix="/boards")


@bp.route("/<board_id>/cards", methods=["POST"])
def create_card(board_id):
    request_body = request.get_json()

    new_card = make_model(Card, request_body, board_id=board_id)

    db.session.add(new_card)
    db.session.commit()

    return jsonify({"card": new_card.to_dict()}), 201