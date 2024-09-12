from application import app, db

# Initialize the app context
with app.app_context():
    db.create_all()

print("Database and tables created!")