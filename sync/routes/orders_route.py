from controllers import order_controller


order_routes = [
    
    (r"/orders", order_controller.OrderHandler),
    (r"/users/([0-9]+)", order_controller.OrderHandler)
]