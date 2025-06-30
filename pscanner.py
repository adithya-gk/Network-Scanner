import socket
banner = """                                                                 
 8888888888',8888' 8 8888888888   8 8888      88    d888888o.   
        ,8',8888'  8 8888         8 8888      88  .`8888:' `88. 
       ,8',8888'   8 8888         8 8888      88  8.`8888.   Y8 
      ,8',8888'    8 8888         8 8888      88  `8.`8888.     
     ,8',8888'     8 888888888888 8 8888      88   `8.`8888.    
    ,8',8888'      8 8888         8 8888      88    `8.`8888.   
   ,8',8888'       8 8888         8 8888      88     `8.`8888.  
  ,8',8888'        8 8888         ` 8888     ,8P 8b   `8.`8888. 
 ,8',8888'         8 8888           8888   ,d8P  `8b.  ;8.`8888 
,8',8888888888888  8 888888888888    `Y88888P'    `Y8888P ,88P' 

"""
print(banner)
ip = input("enter the IP: ")
sport = input("enter starting port no: ")
sport = int(sport)
eport = input("enter ending port: ")
eport = int(eport)

for port in range (sport,eport):
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.settimeout(0.5)
	res = s.connect_ex((ip,port))
	if res == 0:
		print(f"Port {port} is open :)")
	
