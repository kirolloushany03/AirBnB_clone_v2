0x04. AirBnB clone - Web framework
Python - Back-end - Webserver -Flask

Topics covered :
Let's break down flask overview one by one:

1. **What is a Web Framework**:
   A web framework is a pre-built collection of tools, libraries, and patterns that simplifies and standardizes web application development. It provides a structured way to create web applications, handles common tasks like routing, templating, and database interactions, and promotes good coding practices.

2. **How to build a web framework with Flask**:
   Flask is actually a micro web framework for Python, which means it's lightweight and allows developers to choose the components they need. You don't build a web framework with Flask; you use Flask to build web applications. You can, however, create a custom set of extensions, middleware, and functions to extend Flask's capabilities to suit your specific needs.

3. **How to define routes in Flask**:
   In Flask, you define routes using the `@app.route()` decorator. Here's an example:

   ```python
   from flask import Flask

   app = Flask(__name)

   @app.route('/')
   def home():
       return 'Hello, World!'
   ```

4. **What is a route**:
   A route is a URL pattern that specifies a location on your web application. It defines which function or view should be called when a specific URL is accessed. In the example above, `@app.route('/')` defines a route for the root URL ("/") and associates it with the `home()` function.

5. **How to handle variables in a route**:
   You can use route parameters to capture variable parts of the URL. For example:

   ```python
   @app.route('/user/<username>')
   def user_profile(username):
       return f'Profile for {username}'
   ```

   In this example, the `username` variable is captured from the URL and passed as a parameter to the `user_profile()` function.

6. **What is a template**:
   A template is a file that contains the structure and layout of your web page with placeholders for dynamic content. Templates are used to separate the presentation logic (HTML) from the application logic. In Flask, Jinja2 is commonly used for templating.

7. **How to create an HTML response in Flask using a template**:
   To use a template in Flask, you can render it using the `render_template` function from Flask. Here's an example:

   ```python
   from flask import Flask, render_template

   app = Flask(__name)

   @app.route('/')
   def home():
       return render_template('index.html')
   ```

   This code renders the 'index.html' template and returns it as an HTML response.

8. **How to create a dynamic template (loops, conditions, etc.)**:
   You can use Jinja2 template syntax to create dynamic templates in Flask. For loops and conditions, you can do things like:

   ```html
   {% for item in items %}
       {{ item }}
   {% endfor %}

   {% if condition %}
       {{ value }}
   {% else %}
       {{ other_value }}
   {% endif %}
   ```

   These constructs allow you to create dynamic content based on the data you pass to the template.

9. **How to display data from a MySQL database in HTML**:
   To display data from a MySQL database in an HTML template, you need to use a database connection, query the database, retrieve the data, and pass it to your template. Here's a simplified example:

   ```python
   from flask import Flask, render_template
   import mysql.connector

   app = Flask(__name)

   @app.route('/users')
   def list_users():
       # Establish a MySQL connection
       conn = mysql.connector.connect(user='username', password='password', host='localhost', database='mydb')
       cursor = conn.cursor()

       # Execute a query to fetch data
       cursor.execute('SELECT * FROM users')
       users = cursor.fetchall()

       # Close the cursor and connection
       cursor.close()
       conn.close()

       return render_template('users.html', users=users)
   ```

   In the 'users.html' template, you can then use Jinja2 syntax to display the user data.

Remember to handle exceptions, sanitize inputs, and use best practices when dealing with databases to ensure security and reliability in a production environment.