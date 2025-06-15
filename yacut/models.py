from datetime import datetime, timezone

from yacut import db
from .constants import ORIGINAL_MAX_LENGHT, SHORT_MAX_LENGHT


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(ORIGINAL_MAX_LENGHT), nullable=False)
    short = db.Column(db.String(SHORT_MAX_LENGHT), unique=True, nullable=False)
    timestamp = db.Column(db.DateTime, index=True,
                          default=lambda: datetime.now(timezone.utc))
