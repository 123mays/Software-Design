import flask
import psycopg2

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
    conn = psycopg2.connect(
        host="localhost",
        port=5221,
        database="neiroukhm",
        user="neiroukhm",
        password="spring847eyebrow"
    )

     cur = conn.cursor()
     abbrev = abbrev.upper()
     cur.execute("SELECT population FROM us_states WHERE state_code = %s", (abbrev,))
     result = cur.fetchone()
    if result:
        population = result[0]
        return {'state': abbrev, 'population': population}
    else:
        return {'error': 'State not found'}, 404
    return {'if statement didn't work'}
    cur.close()
    conn.close()

if __name__ == '__main__':
    my_port = 5221
    app.run(host='0.0.0.0', port = my_port) 
