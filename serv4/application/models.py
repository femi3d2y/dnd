from application import db



class Effects(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    effect = db.Column(db.String(1000), nullable=False, unique=True)

    def __repr__(self):
        return ''.join([
            'Dice Roll: ',str(self.id), '\r\n',
            'Effect: ', self.effect
        ])
        
class Effects2(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    extreme = db.Column(db.String(1000), nullable=False, unique=True)
    moderate = db.Column(db.String(1000), nullable=False, unique=True)
    gentle = db.Column(db.String(1000), nullable=False, unique=True)

    def __repr__(self):
            return ''.join([
                'Dice Roll: ', self.id, '\r\n',
                'Extreme Effect: ', self.extreme, '\r\n'
                'Moderate Effect: ', self.moderate, '\r\n'
                'Gentle Effect: ', self.gentle, '\r\n'
            ])
