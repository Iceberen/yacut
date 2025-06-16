import random
import string

from .models import URLMap
from .constants import LENGHT_SHOT_LINK


def get_unique_short_id(length=LENGHT_SHOT_LINK):
    """Генерирует уникальный короткий идентификатор переменной длины."""
    chars = string.ascii_letters + string.digits
    while True:
        new_id = ''.join(random.choices(chars, k=LENGHT_SHOT_LINK))
        if URLMap.query.filter_by(short=new_id).first() is None:
            return new_id
