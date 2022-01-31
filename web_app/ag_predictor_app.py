import flask
from flask import request, render_template, redirect
from ag_predictor_api import fund_extract,convert, make_prediction, feature_names, feature_display_names # import from our other python file

#handle HTTP requests
#Importing  the Flask object, 
#and create a function that returns an HTTP response


# import the Flask object from the flask package. 
# You then use it to create your Flask application instance 
# with the name app. You pass the special variable __name__
# that holds the name of the current Python module.
#  It’s used to tell the instance where it’s located—you need this because 
#  Flask sets up some paths behind the scenes.

# Once you create the app instance,
# you use it to handle incoming web requests and send responses to the user.
# @app.route is a decorator that turns a regular Python function into a Flask view function,
# which converts the function’s return value into an HTTP response
# to be displayed by an HTTP client, such as a web browser.
# You pass the value '/' to @app.route() to signify that this 
# function will respond to web requests for the URL /, which is the main URL.

# Initialize the app
app = flask.Flask(__name__)


# An example of routing:
# If they go to the page "/" (this means a GET request
# to the page http://127.0.0.1:5000/), return a simple
# page that says the site is up!
# @app.route("/")
# def hello():
#     return flask.send_file("static/html/index.html")
#     # return 'Hello'
#     # return render_template('index.html')

predictions = [{}]

# decorator to route URL
@app.route("/")
@app.route("/predict", methods=["POST", "GET"])
# GET method is a request you make when you click a link on a website
# POST is like filling out a form

# binding to the function of route 
def predict():
    # request.args contains all the arguments passed by our form
    # comes built in with flask. It is a dictionary of the form
    # "form name (as set in template(html))" (key): "string in the textbox" (value)
    print(request.args)
    fund_vars = fund_extract(request.args)
    print(type(fund_vars))
    global x_input
    x_input = []
    x_input += fund_vars
    #
    cat_vars = convert(request.args.get('category',"Manufacturing"),4,15)
    x_input.extend(cat_vars)
    country_vars = convert(request.args.get('country',"USA"),15,20)
    x_input.extend(country_vars)
    us_state_vars = convert(request.args.get('us_state',"CA"),20,24)
    x_input.extend(us_state_vars)
    x_input.extend([0])

    global predictions
    predictions = make_prediction(x_input)
    # predictions = make_prediction([2.0,182.0, 182.0, 500000.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0])
    # break up the tuple into those two variables
    print(x_input)
    print(predictions)
 ##   if request.method == 'POST':
    # if predictions != [{'name': 'Fail', 'prob': 0.9644768415496009}, {'name': 'Success', 'prob': 0.03552315845039906}]:
    # # if request.args is None:
    # # if x_input != [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0]:
    #     predictions = predictions
 ##        return redirect('/answer/')
    return render_template('predictor.html', x_input=x_input,
                                 feature_names=feature_names,
                                 prediction=predictions,
                                 feature_display_names=feature_display_names)
    # render template uses kwargs (**) which allows unlimited unknown args that can be taken in and do some common thing with all of them
    #feature_names came from predictor_api
    # CSS has to know these names though (x_input, feature_names, prediction)
    # even though flask does not because of kwargs

@app.route("/answer", methods=["POST", "GET"])
def predict2():
    # request.args contains all the arguments passed by our form
    # comes built in with flask. It is a dictionary of the form
    # "form name (as set in template(html))" (key): "string in the textbox" (value)
    print(request.args)
    fund_vars = fund_extract(request.args)
    print(type(fund_vars))
    global x_input
    x_input = []
    x_input += fund_vars
    #
    cat_vars = convert(request.args.get('category',"Manufacturing"),4,15)
    x_input.extend(cat_vars)
    country_vars = convert(request.args.get('country',"USA"),15,20)
    x_input.extend(country_vars)
    us_state_vars = convert(request.args.get('us_state',"CA"),20,24)
    x_input.extend(us_state_vars)
    x_input.extend([0])

    global predictions
    predictions = make_prediction(x_input)
    # predictions = make_prediction([2.0,182.0, 182.0, 500000.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0])
    # break up the tuple into those two variables
    print(x_input)
    print(predictions)
##    #if request.method == 'POST':
    # if predictions != [{'name': 'Fail', 'prob': 0.9644768415496009}, {'name': 'Success', 'prob': 0.03552315845039906}]:
    # # if request.args is None:
    # # if x_input != [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0]:
##    #     predictions = predictions
    #     return redirect('/answer/')


# Flask provides a render_template() helper function 
# that allows use of the Jinja template engine.
# This will make managing HTML much easier by writing your HTML code
# in .html files as well as using logic in your HTML code.
# You’ll use these HTML files, (templates) to build all of your
# application pages, such as the main page where you’ll 
# display the current blog posts, the page of the blog post,
# the page where the user can add a new post, and so on.

    return render_template('answer.html', x_input=x_input,
                                 feature_names=feature_names,
                                 prediction=predictions,
                                 feature_display_names=feature_display_names)


if __name__=="__main__":
    # For local development:
    app.run(debug=True)
    # For public web serving:
    #app.run(host='0.0.0.0')
    #app.run()

# For public web serving:
# app.run(host='0.0.0.0')
