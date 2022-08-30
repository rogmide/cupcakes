from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)

# Model go Below


class Cupcake(db.Model):
    '''Cupcake Model'''

    __tablename__ = 'cupcakes'

    # @classmethod
    # def get_all_users(cls):
    #     '''Get all the user in the DB'''
    #     return cls.query.order_by(User.last_name.asc()).all()

    # @classmethod
    # def get_user_by_id(cls, id):
    #     return cls.query.get(id)

    def __repr__(self):
        '''Better Representation of the class'''
        c = self
        return f'<User id={c.id} flavor={c.flavor} size={c.size} rating={c.rating} >'

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)

    flavor = db.Column(db.String(50),
                       nullable=False,
                       )

    size = db.Column(db.String(50),
                     nullable=False)

    rating = db.Column(db.Float,
                       nullable=False)

    image = db.Column(db.Text,
                      nullable=False,
                      default='https://tinyurl.com/demo-cupcake')

    def serialice(self):
        return {
            'id': self.id,
            'flavor': self.flavor,
            'size': self.size,
            'rating': self.rating,
            'image': self.image,
        }
