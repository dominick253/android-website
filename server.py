from http.server import BaseHTTPRequestHandler, HTTPServer
# Define a basic handler for HTTP requests.
class RequestHandler(BaseHTTPRequestHandler):
    # List of IPs allowed to access this server
    whitelist = ['127.0.0.1']

    def do_GET(self):
        client_ip, _ = self.client_address
        if client_ip in self.whitelist:
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            html_content = """                                                                                                                                                                                                                                                               <html>                                                                                                                                                                                                                                                                           <head>                                                                                                                                                                                                                                                                               <title>Dominick's Android Server Website</title>                                                                                                                                                                                                                                 <style>
                    body {
                        background-color: #121212; /* Dark background */
                        color: #ffffff; /* Light text */                                                                                                                                                                                                                                                 font-family: Arial, sans-serif;                                                                                                                                                                                                                                                  margin: 10px;                                                                                                                                                                                                                                                                    padding: 20px;                                                                                                                                                                                                                                                                   text-align: center;                                                                                                                                                                                                                                                          }                                                                                                                                                                                                                                                                            </style>                                                                                                                                                                                                                                                                     </head>                                                                                                                                                                                                                                                                          <body>                                                                                                                                                                                                                                                                               <h1>Welcome to my Android website!</h1>                                                                                                                                                                                                                                          <h3>This is a website running on ubuntu, on top of android, on a Note 9 phone.</h3>                                                                                                                                                                                              <p>Hello, my name is Dominick. I have been learning programming for over a year now and wanted a fun new project to play around with. So I whipped up a little server and wrote this basic html code. A super fun project all in all. I find building things from the ground up helps me understand the frameworks much better. When I was first learning programing everything was so abstracted from what was going on under the hood it became overwhelming and rather confusing. Now that I have spent time studying the hardware and networking and compilers, the real nuts and bolts of computers, the abstraction of the frameworks is much easier to understand and use. </p>
                <img width=600px height=400px src="https://www.digitaltrends.com/wp-content/uploads/2013/08/server.png"/>
                <p>I have several "real" websites too. Hosted on my proxmox cluster in various forms. I have listed a few of them below if you'd like to view them</p>
                <a href="https://portfolio.dominickp.com">My portfolio website</a>
                <br>
                <a href="https://wordpress.dominickp.com">My wordpress website</a>
                <br>
                <p>If you have noticed I am a dark mode only kind of guy. Just throwing that out there.</p>
            </body>
            </html>
            """
            self.wfile.write(bytes(html_content, "utf-8"))
        else:
            self.send_error(403)

# Set the server's port
server_port = 8000

# Configure and start the server
server_address = ('', server_port)
httpd = HTTPServer(server_address, RequestHandler)
print(f"Server running on port {server_port}...")
httpd.serve_forever()
