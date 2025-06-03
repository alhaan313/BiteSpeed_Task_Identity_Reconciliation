from flask import Blueprint, request, jsonify
from app.models import db, Contact

routes = Blueprint('routes', __name__)

@routes.route('/identify', methods=['POST'])
def identify():
    data = request.get_json()
    email = data.get('email')
    phone = data.get('phoneNumber')

    existing_contacts = Contact.query.filter(
        (Contact.email == email) | (Contact.phone_number == phone)
    ).all()

    if not existing_contacts:
        new_contact = Contact(email=email, phone_number=phone)
        db.session.add(new_contact)
        db.session.commit()

        return jsonify({
            "contact": {
                "primaryContatctId": new_contact.id,
                "emails": [new_contact.email] if new_contact.email else [],
                "phoneNumbers": [new_contact.phone_number] if new_contact.phone_number else [],
                "secondaryContactIds": []
            }
        }), 200