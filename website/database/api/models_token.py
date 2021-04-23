from website import db


class Token(db.Model):
    __tablename__ = 'revoked_tokens'

    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(120))

    @classmethod
    def is_blacklist(cls, jti):
        query = cls.query.filter_by(jti=jti).first()
        return bool(query)
