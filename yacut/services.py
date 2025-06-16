import re

from .models import URLMap
from .utils import get_unique_short_id
from . import db
from .constants import SHORT_LINK_REGEX, INVALID_NAME, SHORT_LINK_EXIST
from .error_handlers import InvalidAPIUsage


def create_short_link(original_url, custom_id=None):
    """Создает объект URLMap, валидирует и сохраняет его в БД."""
    if custom_id:
        if not re.match(SHORT_LINK_REGEX, custom_id):
            raise InvalidAPIUsage(INVALID_NAME)
        if URLMap.query.filter_by(short=custom_id).first():
            raise InvalidAPIUsage(SHORT_LINK_EXIST)
        short_id = custom_id
    else:
        short_id = get_unique_short_id()

    urlmap = URLMap(original=original_url, short=short_id)
    db.session.add(urlmap)
    db.session.commit()
    return urlmap
