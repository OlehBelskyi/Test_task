<h1>REST API</h1>


<h2>app/users</h2>

<h4>GET request (get all users)</h4>

app/users

<h4>POST request (create user)</h4>

json = {
            "name": name,
            "surname": surname,
            "mail": e-mail,
            "login": login,
            "password": password
        }

headers = {
            'Content-Type': 'application/json'
        }





<h2>app/categories</h2>

<h4>GET request (get all users categories)</h4>

app/categories&user_id=<user_id>

<h4>POST request (create category)</h4>

json= {
            "title": title,
            "user_id": user_id
        }

headers = {
            'Content-Type': 'application/json'
        }





<h2>app/items</h2>

<h4>GET request (get all users items)</h4>

app/items&user_id=<user_id>


<h4>POST request (create item)</h4>

json = {
            "image": image,
            "title": title,
            "price": price,
            "user_id": user_id,
            "category_id": category_id,
            "order_id": order_id,
        }

headers = {
            'Content-Type': 'application/json'
        }

