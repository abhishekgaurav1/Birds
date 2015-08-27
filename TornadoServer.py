'''
Created on 27-Aug-2015

@author: Abhishek.Gaurav
'''
import tornado.ioloop
import tornado.web
import os, datetime
import json

class Birds(tornado.web.RequestHandler):
    
    def get(self, request={}):
        try:
            import DbHandler
            dbData = DbHandler.DbHandler()
            if not self.request.body:
                data = dbData.get_all_birds()
                if not data:
                    self.write({})
                    return
                self.write(str(data))
                return
            else:
                try:
                    request = json.loads(self.request.body)
                except Exception, e:
                    request = json.loads(self.request.body.replace("\'","\""))
                if not request:
                    raise tornado.web.HTTPError(400)
                else:                    
                    self.write(str(dbData.get_bird(request["id"])))
                    return 
        except Exception,e:
            raise tornado.web.HTTPError(400)
        
    def post(self, *args, **kwargs):
        try:
            import DbHandler
            dbData = DbHandler.DbHandler()
            try:
                request = json.loads(self.request.body)
            except Exception, e:
                request = json.loads(self.request.body.replace("\'","\""))
            if not request:
                raise tornado.web.HTTPError(400)
            else:
                if "properties" not in request.keys():
                    raise tornado.web.HTTPError(400)
                for key in ["name","family","continents"]:
                    if key not in request["properties"].keys():
                        raise tornado.web.HTTPError(400)
                if "visible" not in request["properties"].keys():
                    request["properties"]["visible"] = {}
                    request["properties"]["visible"]["type"] = False
                if "added" not in request.keys() or not request["properties"]["added"]:
                    utc_datetime = datetime.datetime.utcnow()
                    request["properties"]["added"] = {}
                    request["properties"]["added"]["type"] = utc_datetime.strftime("%Y-%m-%d")
                data = dbData.add_bird(request)
                self.write(str(request))
        except Exception,e:
            raise tornado.web.HTTPError(400)
        
    def delete(self, *args, **kwargs):
        try:
            import DbHandler
            dbData = DbHandler.DbHandler()
            try:
                request = json.loads(self.request.body)
            except Exception, e:
                request = json.loads(self.request.body.replace("\'","\""))
            if not request:
                raise tornado.web.HTTPError(400)
            else:
                print dbData.get_bird(request["id"])
                if dbData.get_bird(request["id"]):
                    print request["id"]
                    dbData.delete_bird(request["id"])
                    return
                else:
                    raise tornado.web.HTTPError(404) 
        except Exception,e:
            raise tornado.web.HTTPError(400)
        
class Application(tornado.web.Application):
    def __init__(self):
        handlers = [(r"/birds", Birds),
                    (r"/birds/", Birds)]
        settings = {
                "debug": True,
                "template_path": os.path.join(os.getcwd(), "templates"),
                "static_path": os.path.join(os.getcwd(), "static")
                }
        tornado.web.Application.__init__(self, handlers, **settings)
        
if __name__ == "__main__":
    application = Application()
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()