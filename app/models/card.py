from app import db

class Card(db.Model):
    card_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    message = db.Column(db.String, nullable=False)
    likes_count = db.Column(db.Integer, nullable=True)
    board_id = db.Column(db.Integer, db.ForeignKey('card.card_id'), nullable=False)
    board = db.relationship("Board", back_populates="cards")

    def to_dict(self):
        return dict(
            id=self.card_id,
            message=self.message,
            likes_count=self.likes_count if self.likes_count else 0
        )
    
    def increase_likes(self):
        self.likes_count += 1