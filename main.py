# import firebase_admin
# from firebase_admin import credentials
from firebase_admin import firestore
from lift_CRUD import get_all_lifts_from_firebase, update_lift_in_firebase, delete_lift_from_firebase, create_lift_in_firebase

# firebaseConfig = {
#     "apiKey": "AIzaSyDHOpI_qVz-VgIOQu6lHhclEEVOC_I_CWk",
#     "authDomain": "ofek-lift-order-system.firebaseapp.com",
#     "projectId": "ofek-lift-order-system",
#     "storageBucket": "ofek-lift-order-system.appspot.com",
#     "messagingSenderId": "527566219284",
#     "appId": "1:527566219284:web:63df22b4af569524311f01",
#     "measurementId": "G-25RM4JEVSR",
#     "databaseURL": "https://ofek-lift-order-system.firebaseio.com"
# }

# Create a Firestore client instance
db = firestore.client()


def main():
    lifts = get_all_lifts_from_firebase()
    print(lifts)
    
    

if __name__ == "__main__":
    main()