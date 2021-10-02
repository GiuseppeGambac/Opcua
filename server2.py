from opcua import ua, uamethod, Server
from opcua.server.user_manager import UserManager
import socket

users_db = {"User" : "Password"}

def user_manager(isession, username, password):
    isession.user = UserManager.User
    return username in users_db and password == users_db[username]

# ip of my computer 
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
url = "opc.tcp://%s:4840" %ip

server = Server()
endpoint = server.set_endpoint(url)
#nome che si vedrà in OPC Expert
servername = "Prova Server"
server.set_server_name(servername)

policyIDs = ["Username"]
server.set_security_IDs(policyIDs)
print(user_manager)
server.user_manager.set_user_manager(user_manager)



root_node = server.get_root_node()
object_node = server.get_objects_node()
idx = server.register_namespace("NamespaceProva")
myobj = object_node.add_object(idx,"variabili")

print(root_node)
print(object_node)
print(myobj)

# dichiarazione con identificatore stringa
temp = myobj.add_variable("ns=2;s=temperatura","temperatura",0,ua.VariantType.Float)
#dichiarazione con identificatore numerico, incrementa di uno ogni volta
temp2 = myobj.add_variable(idx,"temperatura2",0)
temp3 = myobj.add_variable(idx,"temperatura3",15)


temp2.set_writable()
temperatura = 500
temp2.set_value(temperatura)

temp3.set_writable()
temperatura = 500
temp3.set_value(temperatura)


server.start()


