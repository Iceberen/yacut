from flask import abort, flash, redirect, render_template, request, url_for

from . import app, db
from .forms import URLMapForm
from .models import URLMap
from .utils import get_unique_short_id
from .constants import SHORT_LINK_EXIST


@app.route('/', methods=['GET', 'POST'])
def index():
    form = URLMapForm()
    if form.validate_on_submit():
        custom_id = form.custom_id.data
        if custom_id:
            if URLMap.query.filter_by(short=custom_id).first() is not None:
                flash(SHORT_LINK_EXIST)
                return render_template('index.html', form=form)
            short = custom_id
        else:
            short = get_unique_short_id()
        url = URLMap(original=form.original_link.data, short=short)
        short_link = url_for(
            'to_original_view', short_id=short, _external=True
        )
        message = f'<a href="{short_link}">{short_link}</a>'
        flash(message)
        db.session.add(url)
        db.session.commit()
        return render_template('index.html', form=form)

    return render_template('index.html', form=form)


@app.route('/<string:short_id>')
def to_original_view(short_id):
    url_map = URLMap.query.filter_by(short=short_id).first_or_404()
    return redirect(url_map.original)
