from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, URL, Length, Regexp, Optional

from .constants import (ORIGINAL_MIN_LENGHT, ORIGINAL_MAX_LENGHT,
                        SHORT_MAX_LENGHT, SHORT_LINK_REGEX)


class URLMapForm(FlaskForm):
    original_link = URLField(
        'Длинная ссылка',
        validators=[
            DataRequired(message='Обязательное поле'),
            URL(message='Некорректная ссылка.'),
            Length(ORIGINAL_MIN_LENGHT, ORIGINAL_MAX_LENGHT)
        ]
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=[
            Optional(),
            Length(max=SHORT_MAX_LENGHT, message='Максимум 16 символов.'),
            Regexp(SHORT_LINK_REGEX,
                   message='Только латинские буквы и цифры.'),
        ]
    )
    submit = SubmitField('Создать')
