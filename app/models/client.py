from app.extensions import db

class Client(db.Model):
    __tablename__ = "clients"

    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(120), nullable=False)
    contact_email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f"<Client {self.company_name}>"
