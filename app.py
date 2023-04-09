from flask import Flask, request

# create a Flask app
app = Flask(__name__)

# define a route for the /echo endpoint that accepts GET and POST requests
@app.route('/echo', methods=['GET', 'POST'])
def echo():
    # check if the request method is POST
    if request.method == 'POST':
        # extract the JSON data from the request body
        data = request.json

        # return the data as the response
        return data
    else:
        # return a message indicating that the endpoint only accepts POST requests
        return 'This endpoint only accepts POST requests.'

# run the app if this script is executed directly (not imported as a module)
if __name__ == '__main__':
    app.run()