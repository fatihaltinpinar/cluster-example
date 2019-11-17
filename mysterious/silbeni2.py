from bottle import error, route, run, default_app, debug, static_file
from bottle import request
import socket

count = 0

hostname = socket.gethostname()
@route('/')  # Code on the left equals to => route('/', 'GET', index)
def index():
    global count
    count += 1
    page = f'''<html><head><title>counter</title></head><body>
    <h1 style="text-align:center; font-size:100px; color:blue" >{count}</h1>
    <h6 style="text-align:center; font-size:20px" >Hosting pod = {hostname}</h6>
    
    </body></html>'''
    return page


debug(True)
app = default_app()
if __name__ == "__main__":
    run(host="0.0.0.0", port=8080)
