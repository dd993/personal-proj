from flask import Flask, request

# creates a Flask app
app = Flask(__name__)

# defines a route for the /echo endpoint that accepts GET AND POST requests
@app.route('/echo', methods=['GET', 'POST'])
def echo():
    # checks if POST is the request method
    if request.method == 'POST':
        # extract the JSON data from the request body
        data = request.data

        # return the data as the response
        return data
    else:
        # return a message indicating that the endpoint only accepts POST requests
        return 'This endpoint only accepts POST requests.'

# run the app if this script is executed directly (not imported as a module)
if __name__ == '__main__':
    app.run()