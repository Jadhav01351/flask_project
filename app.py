# import the Flask library
from flask import Flask, render_template, request


# Create the Flask instance and pass the Flask constructor the path of the correct module
app = Flask(__name__)


@app.route('/')
def squarenumber():
			return render_template('master_login.html')

# Start with flask web app with debug as True only
# if this is the starting page
if(__name__ == "__main__"):
	app.run(debug=True)
