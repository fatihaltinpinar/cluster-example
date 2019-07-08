from bottle import error, route, run, default_app, debug, static_file
from bottle import request, redirect, response, post, get
import json
import socket

count = 0
restart = False
hostname = socket.gethostname()
@route('/')  # Code on the left equals to => route('/', 'GET', index)
def index():
    global count
    count += 1
    page = f'''<html><head><title>counter</title></head><body>
    <h1 style="text-align:center; font-size:100px; color:blue" >{count}</h1>
    <h6 style="text-align:center; font-size:20px" >Hosting pod = {hostname}</h6>
    <span style="text-align:center"> restart = {restart} </span>
    <form action="/submit" method="post">
    <input type="submit" />
    </form>
    </body></html>'''
    return page

@post('/submit')
def submit():
    global restart
    restart = True
    redirect('/')

@get('/restart')
def get_restart():
    response.headers['Content-Type'] = 'application/json'
    response.headers['Cache-Control'] = 'no-cache'
    return json.dumps({'restart':restart})

debug(True)
app = default_app()
if __name__ == "__main__":
    run(host="0.0.0.0", port=8080)

# <form action="/submit" method="post">
# 						<div class="usernameSection">
# 							<input id="usernameBox" name="username" placeholder="Author" type="text"/>
# 							<div><input name="anonymous" id="anonymousBox" type="checkbox" value="yes"> Write anonymously </div>
# 							<input id="passwordBox" name="password" type="password" placeholder="Password"/>
# 							<input value="Send Comment" type="submit" />
# 						</div>
# 						<input id="commentBox" name="commentText" type="text" placeholder="Enter your toughts here!"/>
# 					# </form>