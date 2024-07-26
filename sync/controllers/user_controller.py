from models.users_model import User
from tornado.web import RequestHandler
from db_init import Session
import json

class UserHandler(RequestHandler):
   
    def post (self):
        user_details = json.loads(self.request.body)
        user_email = user_details['user_email']
        ph_no = user_details['ph_no']
        user_created = user_details['user_created']
        
        with Session() as session:
            user = User(user_email = user_email, ph_no = ph_no, user_created = user_created)
            session.add(user)
            session.commit()
            self.write("User Added.")
        
    def get(self, ph_no):

            session = Session() 
            try:
                user = session.query(User).filter_by(ph_no=ph_no).first()
                if user:
                    self.write(f"User: {user.user_email}, Ph No: {user.ph_no}")
                else:
                    self.write("User not found")
            except Exception as e:
                self.write(f"Error retrieving user: {str(e)}")
            finally:
                session.close()