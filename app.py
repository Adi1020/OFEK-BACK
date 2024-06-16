from flask import Flask, request, jsonify
import firebase_admin
from firebase_admin import credentials, firestore
from lift_CRUD import write_document_to_collection, read_documents_from_collection, update_document_in_collection, delete_document_from_collection

# Initialize Firebase Admin SDK
cred = credentials.Certificate('serviceAccountKey.json')
firebase_admin.initialize_app(cred)

# Create Firestore client
db = firestore.client()

# Initialize Flask app
app = Flask(__name__)

# Route for creating a new document
@app.route('/lifts', methods=['POST'])
def create_lift():
    try:
        document = request.get_json()
        collection_name = 'lifts'
        doc_ref = write_document_to_collection(document, collection_name)
        return jsonify({'id': doc_ref[1].id}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Route for reading all documents
@app.route('/lifts', methods=['GET'])
def read_lifts():
    try:
        collection_name = 'lifts'
        docs = read_documents_from_collection(collection_name)
        return jsonify(docs), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route for updating a document
@app.route('/lifts/<document_id>', methods=['PUT'])
def update_lift(document_id):
    try:
        document = request.get_json()
        collection_name = 'lifts'
        update_document_in_collection(document_id, document, collection_name)
        return jsonify({'message': 'Document updated successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Route for deleting a document
@app.route('/lifts/<document_id>', methods=['DELETE'])
def delete_lift(document_id):
    try:
        collection_name = 'lifts'
        delete_document_from_collection(document_id, collection_name)
        return jsonify({'message': 'Document deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)