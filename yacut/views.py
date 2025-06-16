from flask import flash, redirect, render_template, url_for

from . import app
from .forms import URLMapForm
from .models import URLMap
from .services import create_short_link
from .error_handlers import InvalidAPIUsage


@app.route('/', methods=['GET', 'POST'])
def index():
    form = URLMapForm()
    if form.validate_on_submit():
        custom_id = form.custom_id.data
        original_url = form.original_link.data
        try:
            urlmap = create_short_link(original_url, custom_id)
            short_link = url_for('to_original_view', short_id=urlmap.short,
                                 _external=True)
            message = f'<a href="{short_link}">{short_link}</a>'
            flash(message)
        except InvalidAPIUsage as e:
            flash(e.message)

    return render_template('index.html', form=form)


@app.route('/<string:short_id>')
def to_original_view(short_id):
    url_map = URLMap.query.filter_by(short=short_id).first_or_404()
    return redirect(url_map.original)
