from bottle import route, run, template, static_file, get, post, delete, request, response
from sys import argv
import json
import pymysql

@get("/admin")
def admin_portal():
	return template("pages/admin.html")

# @post("/<category>")
# def category(name):
#     return


connection = pymysql.connect(host="localhost",
                             user="root",
                             password="Belgium14",
                             db="assignment",
                             charset="utf8",
                             cursorclass=pymysql.cursors.DictCursor)

# @post('/save')
# def save_painting():
# user_input = request.get_cookie("user_input")
# try:
#     with connection.cursor() as cursor:
#     query = "INSERT INTO categories (username, name, painting) values ('{}', '{}','{}')".format(
#         username,
#         name,
#         painting
#     )
#     cursor.execute(query)
#     connection.commit()
#     return {"saved": True}
# except Exception as e:
#     response.status = 500
#     response["status__line"] = "error saving painting in the DB"
#     return response

# @post('/category')
# def add_category():
#     user_input = request.forms.get("name")
#     try:
#         with connection.cursor() as cursor:
            # sql = "INSERT INTO categories VALUES {0} {1}".format(user_input,"0921")
            # cursor.execute(sql)
            # results = cursor.fetchall()
            # connection.commit()
            # names = [result['name'] for result in results]
            # if not user_input in names:
            #     add_category(user_input)
            # else:
            #         print("category already in db")
    # except:
    #  return json.dumps({'error'})
        # response.status = 500
        # response["status__line"] = "error saving painting in the DB"
        # return response

# def add_category(user_input):
#     with connection.cursor() as cursor:
#         sql = "INSERT INTO categories VALUES ({0})".format(user_input)
#         cursor.execute(sql)
#         connection.commit()
#         print('category added')

# @post('/signup', method="POST")
# def greet():
#     fname = request.forms.get("user_input")
#     user = {
#         "fname": fname,
#         "lname": lname
#     }
#     return {"user": user}

@get("/")
def index():
    return template("index.html")


@get('/js/<filename:re:.*\.js>')
def javascripts(filename):
    return static_file(filename, root='js')


@get('/css/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='css')


@get('/images/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
    return static_file(filename, root='images')


@post('/category')
def add_category():
    user_input = request.forms.get("name")
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO categories VALUES ('{0}' '{1}')".format(user_input)
            cursor.execute(sql)
            connection.commit()
    except:
        return json.dumps({'error'})

if __name__ == "__main__":
    run(host='localhost', port=8050, debug=True)