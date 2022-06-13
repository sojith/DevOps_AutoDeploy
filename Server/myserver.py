from http.server import HTTPServer, CGIHTTPRequestHandler, BaseHTTPRequestHandler
#from urllib.parse import unquote
#from json.encoder import JSONEncoder
import json
import git
import os
from sojith import smoketest_selenium

class handler_class(CGIHTTPRequestHandler):

    def do_POST(self):
        self.send_response(200, message="Sojith Sugadan")
        self.end_headers()
        print("myserver.py -- " + str(self.headers['Content-Length']))
        payload=str(self.rfile.read(int(self.headers['Content-Length'])))
#        print(payload)
        payload_formatted = payload.replace('b\'','').replace('\'','')
#        print(payload_formatted)  
        payload_json=json.loads(payload_formatted)     
#        print(payload_json)
        print("myserver.py -- " + str(payload_json["repository"]["git_url"]))
        print("myserver.py -- " + "Added"+ str(payload_json["commits"][0]["added"]))
        print("myserver.py -- " + "Removed"+ str(payload_json["commits"][0]["removed"]))
        print("myserver.py -- " + "Updated"+ str(payload_json["commits"][0]["modified"]))

        if (len(payload_json["commits"][0]["added"]) != 0):
            Artifact = str(payload_json["commits"][0]["added"][0])
            Action = "Added"
     
        if (len(payload_json["commits"][0]["modified"]) != 0):
            Artifact = str(payload_json["commits"][0]["modified"][0])
            Action = "Modifed"
            

        gitAction(Artifact, Action) ##To-Do....empty Artifact

        os.system("sh nodeScript.sh")

        smoketest_selenium.smokeTest()


def gitAction(Artifact, Action):
    if (os.path.exists('/home/emperor/Projects/Devops_Project/code/.git') != True):
        print("myserver.py -- " + "Cloning Repository.....")
        git.Repo.clone_from("https://<token-goes-here>@github.com/sojith/DevOps.git","/home/emperor/Projects/Devops_Project/code")
    else:
        rep1 = git.Repo('/home/emperor/Projects/Devops_Project/code/.git')    
        print("myserver.py -- " + "Pulling repository......")
        rep1.remotes.origin.pull()

    print ("myserver.py -- " + Artifact + ' has been ' + Action)

    
    
    

server_class=HTTPServer
#handler_class=BaseHTTPRequestHandler

server_address = ('', 8000)
httpd = server_class(server_address, handler_class)
httpd.serve_forever()

