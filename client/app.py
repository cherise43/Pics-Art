from flask import Flask, request, make_response, jsonify
from flask_migrate import Migrate
from flask_restful import Api
from models import db, User, Pic  
# import app

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///art.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)
api = Api(app)

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json() 
    user_name = data.get('user_name')
    password = data.get('password')
    
    user = User(user_name=user_name, password=password)
    db.session.add(user)
    db.session.commit()

    return jsonify({'message': 'User created successfully'}) 

@app.route('/users', methods=['GET'])  
def get_users():
    users = User.query.all()
    return jsonify([user.serialize() for user in users])

@app.route('/users/<int:user_id>/pics', methods=['POST'])  
def create_pic(user_id): 
    user = User.query.get(user_id) 
    if not user:
        return jsonify({'error': 'User not found'})

    data = request.json
    pic = Pic(user_id=user_id)
    db.session.add(pic)
    db.session.commit()
    return jsonify(pic.serialize())

@app.route('/users/<int:user_id>', methods=['DELETE'])  
def delete_user(user_id):  
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'})
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted'})  

if __name__ == '__main__':
    app.run(port=5000)
