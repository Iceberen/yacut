from .validators import validate_custom_id
from .models import URLMap
from .utils import get_unique_short_id
from . import db


def create_short_link(original_url, custom_id=None):
    """Создает объект URLMap и сохраняет его в БД."""
    if custom_id:
        validate_custom_id(custom_id)
        short_id = custom_id
    else:
        short_id = get_unique_short_id()

    urlmap = URLMap(original=original_url, short=short_id)
    db.session.add(urlmap)
    db.session.commit()
    return urlmap
