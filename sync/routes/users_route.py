from controllers import user_controller


user_routes = [
    
    (r"/users", user_controller.UserHandler),
    (r"/users/(\d+)", user_controller.UserHandler)
]