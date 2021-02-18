Matthew Li-Ah-Kim
mliahkim
1119211104

How to run the web server:
    Option 1: Call the webserver.py through console (python3 webserver.py portnumber) 
        after navigating to the directory.
        portnumber = the port the server to runs on. Default is 12000.
    Option 2: Run it in vscode, including port number or using default. 

How to run the client after server is started:
    Option 1: Call the client.py through console (python3 client.py server_host server_port filename) after navigating to the directory, 
	The variables are:
        	server_host = your ip or hostname. Default is "localhost"
        	server_port = the port the server is running on. Default is "12000"
        	filename = path to the requested object. Default is "/HelloWorld.html"
    Afterwards:
        2. Prints "The response is:  " followed by the HTTP response it received.
        3. It prints out the HTTP file it was given as text. 

How to run with the browser after server is started:
    Put into the browser searchbar-> http://server_host:server_port/filename 
    See the html page, either the HTML file received, or "Error 404 File Not Found" page.
    Check the http message received however you do, 
        For Mac: Enable Developer Mode.
            Open Develop on bar and Show Javascript console
            Hit Network tab
            Then hit filename.html. 
            See HTTP request and HTTP response. 
    

    
        