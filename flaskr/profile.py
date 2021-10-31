from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, session
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('profile', __name__)


@bp.route('/profile', methods=('GET', 'POST'))
@login_required
def profile():
    user_id = session.get('user_id')
    g.user = get_db().execute(
        'SELECT * FROM user WHERE id = ?', (user_id,)
    ).fetchone()
    return render_template('profile/profile.html', user=g.user)
