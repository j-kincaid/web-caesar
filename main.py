from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True


<!--

# TODO: The form uses the POST method.
# There are two inputs: a regular input with type="text" 
# and a textarea.
# Set name="rot" on the input element and name="text" 
# on the textarea.

# The input element has the default value of 0.
# Has a submit button.

# TODO: make a global variable named form above the 
# @app.route("/")decorator preceding the 
# index function, and set its value to be the HTML displayed here.

form = """ <!DOCTYPE html>

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
      <!-- create your form here 

-->
        <form method="POST">
            <div>
                <label for="rot">Rotate by:</label>
                <input type="text" name="rot" value="0">
            </div>
                <textarea name="text" name="text">{rotated}</textarea>
                <br/>
                <input type="submit"></input>
        </form>

    </body>
</html>

"""

# TODO: To process the form, define a new function encrypt in main.py. 
# Add an @app.route decorator to configure the function to receive 
# requests at the root path "/", and with methods=['POST']. When the
# form is submitted, the request will contain the parameters 
# rot and text.


@app.route("/", methods=['POST'])
def index():

# In the index function, return the form variable.
    return form

app.run()

def encrypt(rot, text):
# Add an @app.route decorator to receive requests at
# "/" and with post 
    @app.route("/encrypt", methods=['POST'])
    

# TODO: Encrypt the value of text using rotate_string
# Return the encrypted string to be rendered in the browser. 
# Within encrypt, store the values of these request parameters
# in local variables, converting data types as necessary. 
# Then, encrypt the value of the text parameter using rotate_string. 
# Return the encrypted string wrapped in <h1> tags, to be 
# rendered in the browser.

    encrypt =    """ 

        '<h1>
            <!-- return encrypted string here -->
            {form.format(...)}
            <!-- The argument to this method call should be the empty string in the case of index, and it should be the encrypted string in the case of encrypt -->


        </h1>'

    """
form = form.format(rotated = '')