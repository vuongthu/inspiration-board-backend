from flask import Blueprint, request, jsonify, make_response
from app import db
from app.models.board import Board

bp = Blueprint("boards_bp", __name__, url_prefix="/boards")

#POST/boards
@bp.route("", methods = ["POST"])
def create_board():
    request_body = request.get_json()
    if ("title" not in request_body or 
        "owner" not in request_body):

        return jsonify({"details": "Invalid data"}),

    new_board = Board(
        title=request_body["title"],
        owner=request_body["owner"],)

    db.session.add(new_board)
    db.session.commit()

    return jsonify({"board": new_board.to_dict()}), 201


#GET/boards
@bp.route("", methods=("GET",))
def get_all_boards():
    title_param = request.args.get("title")
    sort_param = request.args.get("sort")

    if title_param:
        boards = Board.query.filter_by(title=title_param)
    else:
        boards = Board.query.all()
    
    result_list = [board.to_dict() for board in boards]
    if sort_param == "asc":
        result_list.sort(key = lambda board: board.get("title").lower())
    
    if sort_param == "desc":
        result_list.sort(reverse = True, key = lambda task : task.get("title").lower())

    return jsonify(result_list), 200



