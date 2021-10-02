from opcua import ua, uamethod, Client,Node
from opcua.server.user_manager import UserManager
import socket


hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
url = "opc.tcp://%s:4840"   %ip

client = Client(url)

client.connect()



print("collegato")




# i = 1 fa riferimento al'oggetto Contenitore variabili e ns = 2 fa riferimento al NameSpace2
myvar = client.get_node("ns=2;i=1").get_children()
#prelevo tutti i valori delle variabili
print(client.get_values(myvar))

print(myvar)
print(myvar[0].get_value())
print(myvar[0].get_browse_name())
print(myvar[1].get_value())
print(myvar[1].get_browse_name())
print(myvar[2].get_value())





stringa = myvar[2].get_browse_name()

def prelevanome(Node):
    nome = Node.get_browse_name()
    return nome.Name

def formatta(Node):
    stringa = prelevanome(Node)
    valore = Node.get_value()
    finale = stringa +":"+str(valore)
    return finale

print(formatta(myvar[2]))


listavariabili = []

"""
while True:
    
    Temp = client.get_node("ns=2;i=2")
    # prendo tutte le variabili
    myvar = client.get_node("ns=2;i=1").get_children()
    
    # prelevo tutti i valori delle variabili     
    print(client.get_values(myvar))
        
        
    temperatura = Temp.get_value()
    if temperatura >= 20:
        Temp.set_value(100)
    
    print(temperatura)
    """
