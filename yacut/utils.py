import random
import string

from .models import URLMap
from .constants import LENGHT_SHOT_LINK


def get_unique_short_id(length=LENGHT_SHOT_LINK):
    """Генерирует уникальный короткий идентификатор переменной длины."""
    chars = string.ascii_letters + string.digits
    for _ in range(100):
        short_id = ''.join(random.choices(chars, k=length))
        if not URLMap.query.filter_by(short=short_id).first():
            return short_id
    raise ValueError('Не удалось сгенерировать уникальный идентификатор.')
