from flask import Blueprint
from marshmallow import Schema, fields

from myapp.models.users import User


bp = Blueprint('api', __name__)


class UserSchema(Schema):
    id = fields.Integer()
    username = fields.String()
    email = fields.String()


@bp.route('/users')
def get_users():
    us = UserSchema()
    users = User.query.all()
    return us.dumps(users, many=True).data
