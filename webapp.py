from flask import Flask, render_template, request 
from db_connect import connect_to_database, execute_query
import os

app = Flask(__name__)

# TAKE THIS OUT WHEN DEPLOYING
app.config['ENV'] = 'development'
app.config['DEBUG'] = True
app.config['TESTING'] = True

# Display homepage
@app.route("/")
def get_home():
    return render_template('index.html')


## Display / Add / Update Customers

@app.route("/customers", methods=['GET', 'POST'])
def get_customers():

    # connect to database
    db_connection = connect_to_database()
    alerts = ()

    if request.method == 'POST':

        # Fetch data from the form
        cust_fname = request.form['first_name']
        cust_lname = request.form['last_name']
        cust_email = request.form['email']
        cust_genre = request.form['genre_id']

        # Create query string and execute command
        # If customer selects "none" as their genre
        if cust_genre == 1:
            query = 'INSERT INTO customers (first_name, last_name, email, genre_id) VALUES (%s, %s, %s, NULL)'
            data = (cust_fname, cust_lname, cust_email)
        else:
            query = 'INSERT INTO customers (first_name, last_name, email, genre_id) VALUES (%s, %s, %s, %s)'
            data = (cust_fname, cust_lname, cust_email, cust_genre)

        execute_query(db_connection, query, data)
        alerts = ("Genres have been updated!", False)

    print('Retrieving Customers data')

    # Create query strings and execute to retrieve required data from database
    query1 = 'SELECT customers.customer_id, customers.first_name, customers.last_name, customers.email, genres.genre_name \
            FROM customers JOIN genres ON customers.genre_id = genres.genre_id'
    result1 = execute_query(db_connection, query1).fetchall()

    query2 = 'SELECT * FROM genres'
    result2 = execute_query(db_connection, query2).fetchall()

    return render_template('customers.html', customers=result1, genres=result2, alerts=alerts)


## Display / Add Genres

@app.route("/genres", methods=['GET', 'POST'])
def genres():

    # connect to database
    db_connection = connect_to_database()
    alerts = ()

    if request.method == 'POST':

        # Fetch data from the form
        genre_name = request.form['genre_name']

        # Create query string and execute command
        query = 'INSERT INTO genres (genre_name) VALUES (%s)'
        data = (genre_name,)
        execute_query(db_connection, query, data)
        alerts = ("Genres have been updated!", False)

    print('Retrieving Genres data')

    # Create query strings and execute to retrieve required data from database
    query = 'SELECT * FROM genres ORDER BY genre_id ASC'
    result = execute_query(db_connection, query).fetchall()

    return render_template('genres.html', genres=result, alerts=alerts)



## Display / Add / Filter Movies

@app.route("/movies", methods=['GET', 'POST'])
def movies():

    # connect to database
    db_connection = connect_to_database()
    alerts = ()

    if request.method == 'POST':

        # Fetch data from the form
        movie_title = request.form['movie_title']
        rental_price = request.form['rental_price']
        studio_id = request.form['studio_id']
        genre_id = request.form['genre_id']

        # Create query string and execute command
        query = 'INSERT INTO movies (movie_title, rental_price, studio_id, genre_id) VALUES (%s, %s, %s, %s)'
        data = (movie_title, rental_price, studio_id, genre_id)
        execute_query(db_connection, query, data)
        alerts = ("Movies have been updated!", False)

    print('Retrieving Movies data')

    # Create query strings and execute to retrieve required data from database

    # If search was used to show tables:
    search_request = request.args.get('searchBar')

	# Check if user uses the search bar
    if search_request is not None:
        query = f"SELECT movies.movie_id, movies.movie_title, movies.rental_price, studios.studio_name, genres.genre_name \
                FROM movies JOIN studios ON movies.studio_id = studios.studio_ID JOIN genres ON movies.genre_id = genres.genre_id \
                WHERE movies.genre_id LIKE (SELECT genre_id FROM genres where genre_name LIKE '%{search_request}%')"
        result = execute_query(db_connection, query).fetchall()
    else:
        query = f'SELECT movies.movie_id, movies.movie_title, movies.rental_price, studios.studio_name, genres.genre_name \
                FROM movies JOIN studios ON movies.studio_id = studios.studio_ID JOIN genres ON movies.genre_id = genres.genre_id'
        result = execute_query(db_connection, query).fetchall()

    query1 = f'SELECT * FROM studios'
    result1 = execute_query(db_connection, query1).fetchall()

    query2 = f'SELECT * FROM genres'
    result2 = execute_query(db_connection, query2).fetchall()

    return render_template('movies.html', movies=result, studios=result1, genres=result2, alerts=alerts)


## Display / Add Studios

@app.route("/studios", methods=['GET', 'POST'])
def studios():

    # connect to database
    db_connection = connect_to_database()
    alerts = ()

    if request.method == 'POST':

        # Fetch data from the form
        studio_name = request.form['studio_name']

        # Create query string and execute command
        # DOESNT WORK
        query = 'INSERT INTO studios (studio_name) VALUES (%s)'
        data = (studio_name,)
        execute_query(db_connection, query, data)
        alerts = ("Studios have been updated!", False)

    print('Retrieving Studios data')

    # Create query strings and execute to retrieve required data from database
    query = 'SELECT * FROM studios'
    result = execute_query(db_connection, query).fetchall()

    return render_template('studios.html', rows=result, alerts=alerts)


# Display / Add Orders and Movies_Orders 

@app.route("/orders", methods=['GET', 'POST'])
def get_orders():

    # connect to database
    db_connection = connect_to_database()
    alerts = ()

    if request.method == 'POST':
        if 'customer_id' in request.form:
        # Fetch data from the form
            cust_id = request.form['customer_id']

            # Create query string and execute command
            query = 'INSERT INTO orders (customer_id) VALUES (%s)'
            data = (cust_id)
            execute_query(db_connection, query, data)
            alerts = ("Orders have been updated!", False)

        elif 'order_id' in request.form:
            order_id = request.form['order_id']
            movie_id = request.form['movie_id']

            query = 'INSERT INTO movies_orders (order_id, movie_id) VALUES (%s, %s)'
            data = (order_id, movie_id)
            execute_query(db_connection, query, data)
            alerts = ("Movies_Orders has been updated!", False)

        print('Retrieving Orders data')

    # Create query strings and execute to retrieve required data from database
    query = 'SELECT orders.order_id, customers.first_name, customers.last_name \
            FROM orders JOIN customers ON orders.customer_id = customers.customer_id \
            ORDER BY orders.order_id ASC'
    result = execute_query(db_connection, query).fetchall()

    query1 = 'SELECT movies_orders.order_id, movies_orders.movie_id, movies.movie_title \
            FROM movies_orders JOIN movies ON movies_orders.movie_id = movies.movie_id \
            ORDER BY movies_orders.order_id ASC, movies_orders.movie_id'
    result1 = execute_query(db_connection, query1).fetchall()

    query2 = 'SELECT * FROM customers'
    result2 = execute_query(db_connection, query2).fetchall()

    query3 = 'SELECT * FROM movies'
    result3 = execute_query(db_connection, query3).fetchall()

    return render_template('orders.html', orders=result, movies_orders=result1, customers=result2, movies=result3, alerts=alerts)


## Delete Orders (and subsequently, Movies_Orders)
@app.route("/deleteOrder/<int:id>", methods=['GET', 'POST'])
def delete_order(id):
    db_connection = connect_to_database()
    alerts = ()

    # Delete from Orders
    disable_fkcheck = 'SET FOREIGN_KEY_CHECKS=0;'
    query = 'DELETE FROM orders WHERE order_id = %s'
    data = (id,)
    execute_query(db_connection, disable_fkcheck)
    execute_query(db_connection, query, data)

    # Delete from Movies_Orders
    query = 'DELETE FROM movies_orders WHERE order_id = %s'
    enable_fkcheck = 'SET FOREIGN_KEY_CHECKS=1;'
    execute_query(db_connection, query, data)
    execute_query(db_connection, enable_fkcheck)

    return get_orders()


# Update a customer's info
@app.route("/updateCustomer/<int:id>", methods=['GET', 'POST'])
def update_cust(id):
    db_connection = connect_to_database()
    alerts = ()

    if request.method == 'GET':
        query1 = 'SELECT * FROM genres'
        result1 = execute_query(db_connection, query1).fetchall()

        return render_template(f'/update.html', id=id, genres=result1, alerts=alerts)

    elif request.method == 'POST':

        # Fetch data from the form
        cust_fname = request.form['first_name']
        cust_lname = request.form['last_name']
        cust_email = request.form['email']
        cust_genre = request.form['genre_id']

        update_query = 'UPDATE customers SET first_name=%s, last_name=%s, email=%s, genre_id=%s WHERE customer_id=%s;'
        data = (cust_fname, cust_lname, cust_email, cust_genre, id)
        result = execute_query(db_connection, update_query, data)
        alerts = (f"Customer {id} has been updated!", True)

        print('Update went through!')

    # Create query strings and execute to retrieve required data from database
    query1 = 'SELECT * FROM customers'
    result1 = execute_query(db_connection, query1).fetchall()

    query2 = 'SELECT * FROM genres'
    result2 = execute_query(db_connection, query2).fetchall()

    return render_template('customers.html', customers=result1, genres=result2, alerts=alerts)

# Listener

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 3157)) 
    app.run(port=port, debug=True) 