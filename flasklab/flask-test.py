import flask

app = flask.Flask(__name__)

#
@app.route('/hello')
def my_function():
    return "Hello World!"

@app.route('/display/<word1>/<word2>')
def my_display(word1, word2):
    the_string = "The words are: " + word1 + " and " + word2;
    return the_string

@app.route('/color/<word1>')
def my_color(word1):
    return '<h1 style="color:Red">' + word1 + '</h1>'

@app.route('/add/<num1>/<num2>')
def addition(num1, num2):
    result = int(num1) + int(num2)
    return str(result)

@app.route('/pop/<abbrev>')
def get_population(abbrev):
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            # Execute query using the state abbreviation, ensuring it matches case in the DB
            cur.execute("SELECT population FROM us_states WHERE state_code = %s", (abbrev.upper(),))
            result = cur.fetchone()
            if result:
                return {'state': abbrev.upper(), 'population': result[0]}
            else:
                # Return an error message if the state is not found
                return {'error': 'State not found'}, 404

    

if __name__ == '__main__':
    my_port = 5221
    app.run(host='0.0.0.0', port = my_port) 
