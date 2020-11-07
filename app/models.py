from flask_sqlalchemy import SQLAlchemy

from run import app

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///livreWeb.db'
db = SQLAlchemy(app)

class Livre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(200), nullable=False)
    tome = db.Column(db.String(200), nullable=True)
    date = db.Column(db.Integer(), nullable=False)
    isbn = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"livre{self.nom}"

def init_db():
    db.drop_all()
    db.create_all()
    db.session.add(Livre(nom="Investigation de scène de crime",
    					 tome="fixation de l'état des lieux et traitement des traces d'objets",
    					 date="2010",
    					 isbn="9782880748456"))
    db.session.add(Livre(nom="Crime et châtiment dans le roman populaire de langue française du XIXe siècle",
    					 tome="actes du colloque international de mai 1992 à Limoges",
    					 date="1994",
    					 isbn="9782910016258"))
    db.session.add(Livre(nom="Crime",
    					 date="2014",
    					 isbn="9782846268653"))
    db.session.add(Livre(nom="Crime and Punishment",
    					 date="2012",
    					 isbn="9780307829603"))
    db.session.add(Livre(nom="Crime, Histoire et Sociétés, 2006/1",
    					 date="2006",
    					 isbn="9782600010894"))
    db.session.add(Livre(nom="D'un crime immotivé",
    					 tome="l'énigme et le passage",
    					 date="1999",
    					 isbn="9782877756563"))
    db.session.add(Livre(nom="Crime and Economy",
    					 tome="Proceedings, Reports Presented to the 11th Criminological Colloquium (1994)",
    					 date="1995",
    					 isbn="9789287128270"))
    db.session.add(Livre(nom="Crime, histoire et sociétés",
    					 tome="Tome 2",
    					 date="2004",
    					 isbn="9782600008990"))
    db.session.add(Livre(nom="Un Crime",
    					 date="1950",
    					 isbn="9780244821227"))
    db.session.commit()


db.create_all()

