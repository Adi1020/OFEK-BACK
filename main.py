# import firebase_admin
# from firebase_admin import credentials
from firebase_admin import firestore
from lift_CRUD import get_all_lifts_from_firebase, update_lift_in_firebase, delete_lift_from_firebase, create_lift_in_firebase


db = firestore.client()


def main():
    lifts = get_all_lifts_from_firebase()
    print(lifts)
    
    

if __name__ == "__main__":
    main()