from flask import Flask, render_template, request  

app = Flask(__name__)  

@app.route('/signup', methods=['GET', 'POST'])  
def signup():  
    if request.method == 'POST':  
        username = request.form['username']  
        password = request.form['password']  
        # Here, you would typically save the user data to a database  
        return f'Success! Username: {username}'  

    # If GET request, display the signup form  
    return '''  
        <form method="post">  
            Username: <input type="text" name="username"><br>  
            Password: <input type="password" name="password"><br>  
            <input type="submit" value="Sign Up">  
        </form>  
    '''  

if __name__ == '__main__':  
    app.run(debug=True)