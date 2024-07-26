from flask import Blueprint, request, jsonify
from app.models import db, Item

bp = Blueprint('main', __name__)

class ItemListView:
    def get(self):
        items = Item.query.all()
        return jsonify([{'id': item.id, 'name': item.name, 'description': item.description} for item in items]), 200

    def post(self):
        data = request.get_json()
        new_item = Item(name=data['name'], description=data.get('description'))
        db.session.add(new_item)
        db.session.commit()
        return jsonify({'id': new_item.id, 'name': new_item.name, 'description': new_item.description}), 201

class ItemDetailView:
    def get(self, id):
        item = Item.query.get_or_404(id)
        return jsonify({'id': item.id, 'name': item.name, 'description': item.description}), 200

    def put(self, id):
        data = request.get_json()
        item = Item.query.get_or_404(id)
        item.name = data['name']
        item.description = data.get('description')
        db.session.commit()
        return jsonify({'id': item.id, 'name': item.name, 'description': item.description}), 200

    def delete(self, id):
        item = Item.query.get_or_404(id)
        db.session.delete(item)
        db.session.commit()
        return '', 204
