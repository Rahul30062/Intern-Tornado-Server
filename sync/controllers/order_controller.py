from tornado.web import RequestHandler
from db_init import Session
from models.orders_model import Order  

class OrderHandler(RequestHandler):
    def get(self, order_id):
        with Session() as session:
            order = session.query(Order).filter_by(id=order_id).first()
            if order:
                self.write(f"Order ID: {order.id}, Product Name: {order.product_name}, Description: {order.product_desc}, Amount: {order.product_amount}, Ordered: {order.product_ordered}")
            else:
                self.set_status(404)
                self.write("Order not found")

    def post(self):
        order_details = self.request.body_arguments  
        product_name = order_details.get('product_name')
        product_desc = order_details.get('product_desc')
        product_amount = order_details.get('product_amount')
        product_ordered = order_details.get('product_ordered')  
        
        with Session() as session:
            order = Order(
                product_name=product_name,
                product_desc=product_desc,
                product_amount=product_amount,
                product_ordered=product_ordered
            )
            session.add(order)
            session.commit()
        
        self.write("Order added successfully")
