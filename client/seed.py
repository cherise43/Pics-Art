from app import db, User, Pic, Sketch


def seed_data():
    user1 = User(user_name='user1', password='password1')
    user2 = User(user_name='user2', password='password2')
    user3 = User(user_name='user3', password='password3')

    # Create pics for user1
    pic1 = Pic(user_id=user1.id, caption='Pic 1', image_url='pic1.jpg')
    pic2 = Pic(user_id=user1.id, caption='Pic 2', image_url='pic2.jpg')

    # Create pics for user2
    pic3 = Pic(user_id=user2.id, caption='Pic 3', image_url='pic3.jpg')

    # Create sketches
    sketch1 = Sketch(title='Sketch 1', description='Sketch 1 description', image_url='sketch1.jpg')
    sketch2 = Sketch(title='Sketch 2', description='Sketch 2 description', image_url='sketch2.jpg')

    # Add objects to the session
    db.session.add_all([user1, user2, user3, pic1, pic2, pic3, sketch1, sketch2])

    # Commit changes to the database
    db.session.commit()

if __name__ == '__main__':
    # Initialize the Flask app and database
    from app import app
    app.app_context().push()
    db.init_app(app)

    # Create database tables
    db.create_all()

    # Seed sample data
    seed_data()
