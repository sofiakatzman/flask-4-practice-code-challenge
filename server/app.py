#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request, make_response
from flask_restful import Resource

# Local imports
from config import app, db, api
from models import Blog, Comment

# Views go here!


class Home(Resource):
    def get(self):
        return {"message": "This works!"}, 200
    
class BlogComments(Resource):
    def get(self):
        blog_comments_list = [{"id" : blog.id, 
                               "title_length" : len(blog.title), 
                               "content_length" : len(blog.content), 
                               "comments": [{"id" : comment.id, 
                                             "comment_text_length": len(comment.content)} for comment in Comment.query.filter_by(blog_id=blog.id)]} for blog in Blog.query.all()]
        response = make_response(
            blog_comments_list, 
            200
        )
        return response

api.add_resource(BlogComments, "/blogs_comments")

class SortedComments(Resource): 
    def get(self):
        comments = [{comment} for comment in Comment.query.all()]
        sorted_comments = sorted(comments.items(), key="content")
        response = make_response(
            sorted_comments, 
            200
        )
        return response

api.add_resource(SortedComments, "/sorted_comments")


if __name__ == '__main__':
    app.run(port=5555, debug=True)
