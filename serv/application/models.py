from application import db



class Effects(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    effect = db.Column(db.String(1000), nullable=False, unique=True)

    def __repr__(self):
        return ''.join([
            'Dice Roll: ', self.id, '\r\n',
            'Effect: ', self.effect
        ])

