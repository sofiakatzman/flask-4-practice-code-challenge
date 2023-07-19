from sqlalchemy_serializer import SerializerMixin

from config import db

# Models go here!


class Blog(db.Model, SerializerMixin):
    __tablename__ = "blogs"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String, nullable=False)

    comments = db.relationship("Comment", backref="blog")

    serialize_rules = ('-comments.blogs.id',)

    def __repr__(self):
        return f'<Blog id={self.id} title="{self.title}" content="{self.content}">'


class Comment(db.Model, SerializerMixin):
    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String, nullable=False)
    blog_id = db.Column(db.Integer, db.ForeignKey("blogs.id"))

    serialize_rules = ('-blogs.comments',)

    def __repr__(self):
        return f'<Comment id={self.id} content="{self.content}" blog_id={self.blog_id}>'
