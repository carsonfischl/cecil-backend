from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('leaderboard', __name__)


@bp.route('/leaderboard', methods=('GET', 'POST'))
def leaderboard():
    db = get_db()
    users = db.execute(
        'SELECT *'
        ' FROM user'
    ).fetchall()
    return render_template('leaderboard/leaderboard.html', users=users)
