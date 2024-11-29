import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
# =============================================================================
conn = sqlite3.connect("sakila.db")
df = pd.read_sql('''
    SELECT
        rental.rental_id, rental.rental_date, rental.return_date,
        customer.last_name AS customer_lastname,
        store.store_id,
        city.city AS rental_store_city,
        film.title AS film_title, film.rental_duration AS film_rental_duration,
        film.rental_rate AS film_rental_rate, film.replacement_cost AS film_replacement_cost,
        film.rating AS film_rating
    FROM rental
    INNER JOIN customer ON rental.customer_id == customer.customer_id
    INNER JOIN inventory ON rental.inventory_id == inventory.inventory_id
    INNER JOIN store ON inventory.store_id == store.store_id
    INNER JOIN address ON store.address_id == address.address_id
    INNER JOIN city ON address.city_id == city.city_id
    INNER JOIN film ON inventory.film_id == film.film_id
    ;
''', conn, index_col='rental_id', parse_dates=['rental_date', 'return_date'])
a = np.array(2**3 , dtype=np.int8)
b = np.array([0.1, 2, 3, 4])
c = np.array([0.1, 2, 3, 4], dtype = np.float16)
c = np.array([[1,1,1,1],[2,2,2,2]])
c[0]
c[-1]
c[:,2]
c.shape
c.size
c.ndim
Df=df.drop(["rental_date", "return_date", "customer_lastname", "rental_store_city", "film_title", "film_rating"],  axis = 1)
d = Df.to_numpy()
c[1] = [3,3,3,3]
c[1] = 2
d=c+1
c += 1
g = [1,2,3,4]
[i*10 for i in g]
l = np.arange(4)
l >= 2
l[l >= 2]
Df>=10
DF=Df[Df >= 10]
l[l >= l.mean()]
c -= 1
c = c.T
c = np.transpose(c)
c.dot(d)

h = list(range(100000))
k = np.arange(100000)
%time np.sum(k**2)             # square all the elements of array and then sum them
%time sum([x**2 for x in h])