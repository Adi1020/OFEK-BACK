import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase Admin SDK
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

# Create Firestore client
db = firestore.client()


def get_all_lifts_from_firebase():
    docs = db.collection("lifts").stream()
    return [doc.to_dict() for doc in docs]


def update_lift_in_firebase(document_id, document):
    doc_ref = db.collection("lifts").document(document_id)
    doc_ref.set(document)
    return doc_ref


def delete_lift_from_firebase(document_id):
    db.collection("lifts").document(document_id).delete()
    return None


def create_lift_in_firebase(document):
    doc_ref = db.collection("lifts").add(document)
    return doc_ref


