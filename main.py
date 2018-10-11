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
        <form method="POST">
            <div>
                <label for="rot">Rotate by:</label>
                <input type="text" name="rot" value="0">
            </div>
                <textarea name="text" name="text">{}</textarea>
                <br/>
                <input type="button">Submit Query</input>
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
      {form.format(...)}
      <!-- The argument to this method call should be the empty string in the case of index, and it should be the encrypted string in the case of encrypt -->
</h1>'


"""