from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), nullable=False)
    firstname = db.Column(db.String(250), nullable=False)
    lastname = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), unique=True, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email
        }

class Follower(db.Model):
    __tablename__ = 'follower'
    user_from_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    user_to_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)

class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship(User)

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id
        }

class Media(db.Model):
    __tablename__ = 'media'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Enum('image', 'video', name='media_types'))
    url = db.Column(db.String(250))
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    post = db.relationship(Post)

    def serialize(self):
        return {
            "id": self.id,
            "type": self.type,
            "url": self.url
        }

class Comment(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key=True)
    comment_text = db.Column(db.String(250), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    user = db.relationship(User)
    post = db.relationship(Post)

    def serialize(self):
        return {
            "id": self.id,
            "comment_text": self.comment_text,
            "author_id": self.author_id
        }