from db_init import Base,engine
import tornado.web
import asyncio
from routes.users_route import user_routes
from routes.orders_route import order_routes

#   Sync Server Creation


def main():
    Base.metadata.create_all(engine)
    
    routes = user_routes + order_routes
    
    app=tornado.web.Application(routes)
    app.listen(8080)
    print("Sync server started on port 8080")
    tornado.ioloop.IOLoop.current().start()
    
if __name__ =="__main__":
    main()