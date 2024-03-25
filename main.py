from flask import request, jsonify
from config import app, db
from models import Contact


@app.route("/contacts", methods=["GET"])
def get_contacts():

    # Get the contacts as python objects
    contacts = Contact.query.all()
    json_contacts = list(map(lambda contact: contact.to_json(), contacts))
    return jsonify({"contacts": json_contacts})


@app.route("/create_contact", methods=["POST"])
def create_contact():
    first_name = request.json.get("firstName")
    last_name = request.json.get("lastName")
    email = request.json.get("email")

    if not first_name or last_name or email:
        return jsonify({"Message": "You need to provide data!"}, 400)

    # We create the new contact
    new_contact = Contact(first_name=first_name, last_name=last_name, email=email)

    # Then try to add it to the database
    try:
        db.session.add(new_contact)
        db.session.commit()
    except Exception as e:
        return jsonify({"Error": str(e)}, 400)

    return jsonify({"Message": "User added!"}, 201)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
