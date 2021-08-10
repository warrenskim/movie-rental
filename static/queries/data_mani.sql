-- Data Manipulation Queries

-- genres
-- get all available genres
-- insert new genre
SELECT * FROM genres;
INSERT INTO genres (genre_name) VALUES (:genre_name_Input);


-- customers
-- get all customers in the DB
-- insert new customer
SELECT * FROM customers;
INSERT INTO customers (first_name, last_name, email, genre_id)
VALUES
    (:first_name_input, :last_name_input, :email_input, :genre_id_input);

-- update an existing customer
UPDATE customers
SET first_name=:first_name_input, last_name=:last_name_input, email=:email_input, genre_id=:genre_id_input
WHERE customer_id=:selected_customer_id;


-- movies
-- get all movies from a certain genre
-- insert new movie
SELECT * FROM movies WHERE genre_id=:selected_genre;
INSERT INTO movies (movie_title, rental_price, studio_id, genre_id)
VALUES
    (:movie_title_Input, :rental_price_Input, :studio_id_Input, :genre_id_Input);


-- studios
-- get all studios 
-- insert new studio
SELECT * FROM studios;
INSERT INTO studios (studio_name) VALUES (:studio_name_input);


-- orders
-- get all orders 
-- insert new order
SELECT * FROM orders;
INSERT INTO orders (customer_id)
VALUES
    (:customer_id_input);

-- delete an order
DELETE FROM orders WHERE order_id==:selected_order_id;

-- movies_orders
-- get all movies linked to orders 
-- insert new movie linked to order
SELECT * FROM movies_orders;
INSERT INTO movies_orders (order_id, movie_id) 
VALUES 
    (:order_id_input, :movie_id_input);

-- delete a link between an order and movie
DELETE FROM movies_orders WHERE order_id==:selected_order_id;
