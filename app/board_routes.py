from flask import Blueprint, request, jsonify, make_response
from app import db

bp = Blueprint("boards_bp", __name__, url_prefix="/boards")
