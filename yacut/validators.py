import re

from .constants import SHORT_LINK_REGEX
from .models import URLMap
from .error_handlers import InvalidShortID, ShortIDAlreadyExists


def validate_custom_id(custom_id):
    """Проверяет корректность и уникальность пользовательского короткого ID."""
    if not re.match(SHORT_LINK_REGEX, custom_id):
        raise InvalidShortID()
    if URLMap.query.filter_by(short=custom_id).first():
        raise ShortIDAlreadyExists()
