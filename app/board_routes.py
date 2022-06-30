from crypt import methods
from flask import Blueprint, request, jsonify, make_response
from app import db
from app.models.board import Board
from app.models.card import Card
from .routes_helper import error_msg, success_msg, make_model, get_model_by_id

bp = Blueprint("boards_bp", __name__, url_prefix="/boards")

#POST/boards
@bp.route("", methods=["POST"])
def create_board():
    request_body = request.get_json()

    new_board = make_model(Board, request_body)

    db.session.add(new_board)
    db.session.commit()

    return jsonify({"board": new_board.to_dict()}), 201


#GET/boards
@bp.route("", methods=("GET",))
def get_all_boards():

    boards = Board.query.order_by("board_id").all()
    
    board_list = [board.to_dict() for board in boards]

    return jsonify(board_list), 200

    #def get_all_task():
    # sort_query = request.args.get("sort")
    # if sort_query == "asc":
    #     tasks = Task.query.order_by(Task.title.asc())
    # elif sort_query == "desc":
    #     tasks = Task.query.order_by(Task.title.desc())
    # else:
    #     tasks = Task.query.all()
    # tasks_response = []
    # for task in tasks:
    #     tasks_response.append(task.to_json())


@bp.route("/<board_id>/cards", methods=["POST"])
def create_card(board_id):
    request_body = request.get_json()

    new_card = make_model(Card, request_body, board_id=board_id)

    db.session.add(new_card)
    db.session.commit()

    return jsonify({"card": new_card.to_dict()}), 201


