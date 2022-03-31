from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
import os

app=Flask(__name__)
api=Api(app)
user=os.environ.get('USER')
password=os.environ.get('PASSWORD')
host=os.environ.get('HOST')

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://'+user+':'+password+'@'+host+':5432/librarybooks'
db=SQLAlchemy(app)

class BookModel(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String, nullable=False)
    authorname = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"Books(name={name}, authorname = {authorname})"

db.create_all()

books_post_args=reqparse.RequestParser()
books_post_args.add_argument("name", type=str, help="Name of books")
books_post_args.add_argument("authorname", type=str, help="Name of Writer")

books_patch_args=reqparse.RequestParser()
books_patch_args.add_argument("name", type=str, help="Name of books")
books_patch_args.add_argument("authorname", type=str, help="Name of Writer")

resource_fields= {
    'id': fields.Integer,
    'name' : fields.String,
    'authorname' : fields.String
}
class Books(Resource):
    @marshal_with(resource_fields)
    def get(self, book_id):
        result = BookModel.query.filter_by(id=book_id).first()
        if not result: 
           abort (http_status_code=404, message='Could not find book with that id')
        return result

    @marshal_with(resource_fields)
    def post(self, book_id):
        args=books_post_args.parse_args()
        result = BookModel.query.filter_by(id=book_id).first()

        if result: 
            abort(http_status_code=409, message="Book id taken...")

        book=BookModel(id=book_id, 
                    name=args['name'], 
                    authorname =args['authorname'])
        db.session.add(book)
        db.session.commit()
        return book, 201

    @marshal_with(resource_fields)
    def patch(self,book_id):
        result = BookModel.query.filter_by(id=book_id).first()
        if not result:
            abort(http_status_code=404, message="Book id not found")

        args=books_patch_args.parse_args()

        if args['name']:
            result.name=args['name']

        if args['authorname']:
            result.authorname=args['authorname']

        db.session.commit()
        return result, 200

    @marshal_with(resource_fields)
    def delete(self, book_id):
        result = BookModel.query.filter_by(id=book_id).first()
        if not result:
            abort(http_status_code=404, message='Could not delete as no book exist with that id')
        
        db.session.delete(result)
        db.session.commit()
        return '',204

api.add_resource(Books,"/books/<int:book_id>")

if __name__ == "__main__":
    app.run(debug=True)


