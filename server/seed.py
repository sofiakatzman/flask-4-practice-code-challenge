#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, Blog, Comment

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Starting seed...")

        Comment.query.delete()
        Blog.query.delete()
        db.session.commit()

        blog_1 = Blog(title="Title 1", content="Content 1")
        blog_2 = Blog(title="Title 2", content="Content 2")
        blog_3 = Blog(title="Title 3", content="Content 3")

        db.session.add_all([blog_1, blog_2, blog_3])
        db.session.commit()

        # blog 1 comments
        comment_1 = Comment(content="hello", blog_id=blog_1.id)
        comment_2 = Comment(content="goodbye", blog_id=blog_1.id)
        comment_3 = Comment(content="sunshine", blog_id=blog_1.id)

        db.session.add_all([comment_1, comment_2, comment_3])
        db.session.commit()

        # blog 2 comments
        comment_4 = Comment(content="bob", blog_id=blog_2.id)
        comment_5 = Comment(content="pizza", blog_id=blog_2.id)
        comment_6 = Comment(content="sara", blog_id=blog_2.id)

        db.session.add_all([comment_4, comment_5, comment_6])
        db.session.commit()

        # blog 3 comments
        comment_7 = Comment(
            content="excellent post about why python is the greatest", blog_id=blog_3.id)
        comment_8 = Comment(content="peter parker", blog_id=blog_3.id)
        comment_9 = Comment(content="yellow marker", blog_id=blog_3.id)

        db.session.add_all([comment_7, comment_8, comment_9])
        db.session.commit()
