-- Create tables
SET FOREIGN_KEY_CHECKS = 0;
DROP TABLE IF EXISTS movies_orders;
DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS studios;
DROP TABLE IF EXISTS movies;
DROP TABLE IF EXISTS genres;
SET FOREIGN_KEY_CHECKS = 1;

-- create genres table
CREATE TABLE genres (
genre_id int NOT NULL AUTO_INCREMENT,
genre_name varchar(255) UNIQUE NOT NULL,
PRIMARY KEY (genre_id)
) ENGINE=InnoDB;

-- create customers table
CREATE TABLE customers (
customer_id int NOT NULL UNIQUE AUTO_INCREMENT,
first_name varchar(255) NOT NULL,
last_name varchar(255) NOT NULL,
email varchar(255) NOT NULL,
genre_id int,
FOREIGN KEY(genre_id) REFERENCES genres (genre_id),
PRIMARY KEY (customer_id)
) ENGINE=InnoDB;

-- create orders table
CREATE TABLE orders (
order_id int NOT NULL UNIQUE AUTO_INCREMENT,
customer_id int NOT NULL,
PRIMARY KEY (order_id),
FOREIGN KEY(customer_id) REFERENCES customers (customer_id)
) ENGINE=InnoDB;

-- studios table
CREATE TABLE studios (
studio_id int NOT NULL UNIQUE AUTO_INCREMENT,
studio_name varchar(255) NOT NULL,
    PRIMARY KEY (studio_id)
) ENGINE=InnoDB;

-- create movies table
CREATE TABLE movies (
movie_id int(11) NOT NULL AUTO_INCREMENT,
movie_title varchar(255) UNIQUE NOT NULL,
rental_price int NOT NULL,
studio_id int NOT NULL,
genre_id int NOT NULL,
FOREIGN KEY(studio_id) REFERENCES studios (studio_id),
FOREIGN KEY(genre_id) REFERENCES genres (genre_id),
PRIMARY KEY (movie_id)
) ENGINE=InnoDB;

-- create movies_orders table
CREATE TABLE movies_orders (
order_id int NOT NULL,
movie_id int NOT NULL,
FOREIGN KEY(order_id) REFERENCES orders (order_id),
FOREIGN KEY(movie_id) REFERENCES movies (movie_id),
PRIMARY KEY (order_id, movie_id)
) ENGINE=InnoDB;


-- setting auto_increment values and start point
ALTER TABLE genres AUTO_INCREMENT = 1;
ALTER TABLE customers AUTO_INCREMENT = 1;
ALTER TABLE orders AUTO_INCREMENT = 1;
ALTER TABLE movies AUTO_INCREMENT = 1;
ALTER TABLE studios AUTO_INCREMENT = 1;

SET @@auto_increment_increment=1;


-- insert data into studios table
INSERT INTO studios (studio_name)
VALUES
    ('Mandate Pictures'),
    ('Columbia Pictures'),
    ('Warner Animation Group'),
    ('Marvel Studios'),
    ('DC Films'),
    ('Lucasfilm'),
    ('Fox Searchlight Pictures'),
    ('Warner Bros Pictures'),
    ('Summit Entertainment');

-- insert data into genres table
INSERT INTO genres (genre_name)
VALUES
    ('None'),
    ('Action'),
    ('Comedy'),
    ('Romance');

-- insert data into customers table
INSERT INTO customers (first_name, last_name, email, genre_id)
VALUES
    ('Eric', 'Chiu', 'eric21@gmail.com', 
		(SELECT genre_id FROM genres WHERE genre_name="Action")),
    ('Warren', 'Kim', 'warren@hello.com', 
		(SELECT genre_id FROM genres WHERE genre_name="Comedy")),
    ('Pamela', 'Beasley', 'pam@dundermifflin.com', 
		(SELECT genre_id FROM genres WHERE genre_name="Romance")),
    ('Michael', 'Scott', 'mike@dundermifflin.com', 
		(SELECT genre_id FROM genres WHERE genre_name="Comedy")),
    ('Louise', 'Belcher', 'louise@wagstaff.com', 
		(SELECT genre_id FROM genres WHERE genre_name="Action")),
    ('Tina', 'Belcher', 'tina@wagstaff.com', 
		(SELECT genre_id FROM genres WHERE genre_name="Romance")),
    ('Piper', 'Chapman', 'piper@litchfield.com', 
		(SELECT genre_id FROM genres WHERE genre_name="Action"));

-- insert data into orders table
INSERT INTO orders (customer_id)
VALUES
    (7),
    (5),
    (4),
    (1),
    (6),
    (2),
    (3);

-- insert data into movies table
INSERT INTO movies (movie_title, rental_price, studio_id, genre_id) 
VALUES
    ('The Lego Movie', 3, 
        (SELECT studio_id FROM studios WHERE studio_name='Warner Animation Group'), 
        (SELECT genre_id FROM genres WHERE genre_name='Comedy')),
    ('This is the End', 3, 
        (SELECT studio_id FROM studios WHERE studio_name='Mandate Pictures'),
        (SELECT genre_id FROM genres WHERE genre_name='Comedy')),
    ('21 Jump Street', 3, 
        (SELECT studio_id FROM studios WHERE studio_name='Columbia Pictures'),
        (SELECT genre_id FROM genres WHERE genre_name='Comedy')),
    ('Iron Man', 3, 
        (SELECT studio_id FROM studios WHERE studio_name='Marvel Studios'),
        (SELECT genre_id FROM genres WHERE genre_name='Action')),
    ('Wonder Woman', 3, 
        (SELECT studio_id FROM studios WHERE studio_name='DC Films'),
        (SELECT genre_id FROM genres WHERE genre_name='Action')),
    ('Black Panther', 3, 
        (SELECT studio_id FROM studios WHERE studio_name='Marvel Studios'),
        (SELECT genre_id FROM genres WHERE genre_name='Action')),
    ('A Star is Born', 3, 
        (SELECT studio_id FROM studios WHERE studio_name='Warner Bros Pictures'),
        (SELECT genre_id FROM genres WHERE genre_name='Romance')),
    ('500 Days of Summer', 3, 
        (SELECT studio_id FROM studios WHERE studio_name='Fox Searchlight Pictures'),
        (SELECT genre_id FROM genres WHERE genre_name='Romance')),
    ('La La Land', 3, 
        (SELECT studio_id FROM studios WHERE studio_name='Summit Entertainment'),
        (SELECT genre_id FROM genres WHERE genre_name='Romance'));

-- insert data into movies_orders table
INSERT INTO movies_orders (order_id, movie_id)
VALUES
    (1, 3),
    (1, 4),
    (1, 8),
    (1, 9),
    (2, 1),
    (2, 2),
    (2, 3),
    (2, 4),
    (2, 5),
    (2, 6),
    (2, 7),
    (2, 8),
    (2, 9),
    (3, 1),
    (3, 3),
    (3, 6),
    (3, 7),
    (3, 8),
    (4, 2),
    (4, 5),
    (4, 6),
    (5, 5),
    (6, 1),
    (6, 7),
    (7, 1),
    (7, 2),
    (7, 3),
    (7, 5),
    (7, 7),
    (7, 8),
    (7, 9);
