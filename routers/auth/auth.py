from flask import render_template, request, redirect, session
from app import app

@app.route('/')
def auth():
    return render_template('auth.html')



# @app.route('/login', methods=['GET', 'POST'])
# def login():
# #     if request.method == 'POST':
# #         username = request.form.get('username')
# #         password = request.form.get('password')
# # #        user_id = UserInfo.get_user(username, password)
# #         # if user_id:
# #         #     session['username'] = username
# #         #     session["user_id"] = user_id
# #         #     return redirect('/dashboard')
# #         else:
# #             return 'Неверный логин или пароль'
#     return render_template('login.html')

# @app.route("/register", methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         username = request.form.get('username')
#         password = request.form.get('password')

# #        UserInfo.create_account(username, password)

#         return f"<h2>Пользователь {username} зарегистрирован!</h2><a href='/login'>Перейти ко входу</a>"

#     return render_template('register.html')