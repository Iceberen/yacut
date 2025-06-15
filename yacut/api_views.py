import re
from flask import jsonify, request, url_for

from . import app, db
from .models import URLMap
from .error_handlers import InvalidAPIUsage
from .utils import get_unique_short_id
from .constants import (SHORT_LINK_REGEX, REQUEST_BODY_IS_MISSING,
                        REQUIRED_FIELD, INVALID_NAME, NOT_FOUND, 
                        SHORT_LINK_EXIST)


@app.route('/api/id/', methods=['POST'])
def add_url():
    data = request.get_json(force=True, silent=True)
    if data is None:
        raise InvalidAPIUsage(REQUEST_BODY_IS_MISSING)
    if 'url' not in data:
        raise InvalidAPIUsage(REQUIRED_FIELD)

    if 'custom_id' in data:
        short_id = data['custom_id']
        if short_id == '':
            short_id = get_unique_short_id()
        if re.match(SHORT_LINK_REGEX, short_id) is None:
            raise InvalidAPIUsage(INVALID_NAME)
        if URLMap.query.filter_by(short=short_id).first() is not None:
            raise InvalidAPIUsage(SHORT_LINK_EXIST)
        short = short_id
    else:
        short = get_unique_short_id()
    original = data['url']
    urlmap = URLMap(original=original, short=short)
    db.session.add(urlmap)
    db.session.commit()
    short_link = url_for('to_original_view', short_id=short, _external=True)
    return (jsonify({'url': original, 'short_link': short_link}), 201)


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_url(short_id):
    url = URLMap.query.filter_by(short=short_id).one_or_none()
    if url is None:
        raise InvalidAPIUsage(NOT_FOUND, 404)
    return jsonify({'url': url.original}), 200
