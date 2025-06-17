from flask import jsonify, request, url_for

from . import app
from .models import URLMap
from .error_handlers import (InvalidAPIUsage, InvalidShortID,
                             ShortIDAlreadyExists)
from .constants import REQUEST_BODY_IS_MISSING, REQUIRED_FIELD, NOT_FOUND
from .services import create_short_link
from .constants import INVALID_NAME, SHORT_LINK_EXIST


@app.route('/api/id/', methods=['POST'])
def add_url():
    data = request.get_json(force=True, silent=True)
    if data is None:
        raise InvalidAPIUsage(REQUEST_BODY_IS_MISSING)
    if 'url' not in data:
        raise InvalidAPIUsage(REQUIRED_FIELD)

    original_url = data['url']
    custom_id = data.get('custom_id')
    try:
        urlmap = create_short_link(original_url, custom_id)
    except InvalidShortID:
        raise InvalidAPIUsage(INVALID_NAME)
    except ShortIDAlreadyExists:
        raise InvalidAPIUsage(SHORT_LINK_EXIST)
    short_link = url_for('to_original_view', short_id=urlmap.short,
                         _external=True)
    return (jsonify({'url': urlmap.original, 'short_link': short_link}), 201)


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_url(short_id):
    url = URLMap.query.filter_by(short=short_id).one_or_none()
    if url is None:
        raise InvalidAPIUsage(NOT_FOUND, 404)
    return jsonify({'url': url.original}), 200
