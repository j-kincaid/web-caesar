from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form =""" <!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
        <form action="/encrypt" method="POST">
            <label for="rot">Rotate by:</label>
            <input type="text" name="rot" value= 0 />
            <input type="button">Submit Query</input>
            <textarea name="text" />
        </form>

      <!-- create your form here -->
    </body>
</html>

"""
@app.route("/")
def index():
    return form

app.run()

def encrypt(rot, text):
# Add an @app.route decorator to receive requests at
# "/" and with post 
    @app.route("/", methods=['POST'])
    

# Encrypt the value of text using rotate_string
# Return the encrypted string to be rendered in the browser. 
encrypted = """ 

'<h1>
      <!-- return encrypted string here -->
</h1>'


"""