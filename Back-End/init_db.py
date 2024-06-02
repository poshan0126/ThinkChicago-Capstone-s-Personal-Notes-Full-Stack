from app import create_app, db
from app.models import Category

def create_tables():
    app = create_app()
    with app.app_context():
        db.create_all()

        # Predefined categories
        predefined_categories = ['Story', 'Moments', 'Emotions']

        for category_name in predefined_categories:
            category = Category.query.filter_by(name=category_name).first()
            if category is None:
                category = Category(name=category_name)
                db.session.add(category)

        db.session.commit()

if __name__ == '__main__':
    create_tables()
