from flaskext.mysql import MySQL
from flask import (Flask, request, session, g, redirect, url_for, abort, render_template, flash, Response)
import os
from werkzeug.utils import secure_filename
import calendar
import time
from  PIL import Image
from datetime import date

mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'online_shopping'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route('/signup',methods = ['POST', 'GET'])
def signup():
   if request.method == 'POST':
      User_name = request.form['user_name']
      Address = request.form['address']
      Phone_number = request.form['phone_number']
      Email_id = request.form['email_id']
      Password = request.form['password']
      User_type = 'buyer'
      qry = " INSERT INTO `user_details` ( User_name, Address, Phone_number, Email_id, Password, User_type ) values " 
      qry += "('"+User_name +"','"+Address +"','"+Phone_number +"','"+Email_id +"','"+Password +"','"+User_type +"')"
      conn = mysql.connect()
      cursor = conn.cursor()
      cursor.execute(qry)
      conn.commit()
      session['username'] = Email_id
      session['user_type'] = User_type
      session['user_id'] = str(cursor.lastrowid)
      flash("Welcome to Estore.")
      return redirect(url_for('index'))
   return render_template('signup.html')

@app.route('/buyer_signup',methods = ['POST', 'GET'])
def buyer_signup():
   if request.method == 'POST':
      User_name = request.form['user_name']
      Address = request.form['address']
      Phone_number = request.form['phone_number']
      Email_id = request.form['email_id']
      Password = request.form['password']
      User_type = 'seller'
      qry = " INSERT INTO `user_details` ( User_name, Address, Phone_number, Email_id, Password, User_type ) values " 
      qry += "('"+User_name +"','"+Address +"','"+Phone_number +"','"+Email_id +"','"+Password +"','"+User_type +"')"
      conn = mysql.connect()
      cursor = conn.cursor()
      cursor.execute(qry)
      conn.commit()
      flash("Buyer Id Created Sucessfully")
      return redirect(url_for('buyer_signup'))
   return render_template('buyer_signup.html')   
 
@app.route('/logout')
def logout():
   session.pop('username', None)
   session.pop('user_id', None)
   session.pop('user_type', None)
   return redirect(url_for('index'))

@app.route('/login',methods = ['POST', 'GET'])
def login():

   if request.method == 'POST':
      email_id = request.form['name']
      password = request.form['password']
      cursor = mysql.connect().cursor()
      cursor.execute("SELECT * from user_details where email_id='" + email_id + "' and password='" + password + "'")
      data = cursor.fetchone()
      if data is None:
         flash( "Username or Password is wrong")
         return render_template('login.html')
      else:
         if data[7] == 1 :
            flash( "User blocked")
            return render_template('login.html')
         else :
            session['username'] = email_id
            session['user_type'] =  data[6]
            session['user_id'] = data[0]
            return redirect(url_for('product_list'))
   else:
      return render_template('login.html')

@app.route('/product_list')
def product_list():

      qry =  "SELECT * FROM `product_details` "
      conn = mysql.connect()
      cursor = conn.cursor()
      cursor.execute(qry)
      data = cursor.fetchall()
      print("product_list "+str(data))
      return render_template("product_list.html",data=data)

   
@app.route('/insert_product', methods=['GET', 'POST'])
def insert_product():
  
   if request.method == 'POST':
      name = request.form['name']
      desc = request.form['desc']
      cost = request.form['cost']
      user_id = session['user_id']
      f = request.files['image']
      filename = secure_filename(f.filename)
      base = os.path.splitext(filename)[1]
      ts = calendar.timegm(time.gmtime())
      file_name =  str(ts)+base
      f.save("static/pic_uploads/"+ file_name)
      destloc = "static/pic_uploads/"+ file_name
      qry = "INSERT INTO `product_details`(`product_name`, `description`, `price`,`image_path`, `user_id`) VALUES ('"+name+"','"+desc+"','"+str(cost)+"', '"+destloc+"' , '"+str(user_id)+"')"
      conn = mysql.connect()
      cursor = conn.cursor()
      cursor.execute(qry)
      print(qry)
      conn.commit()
      flash("New product added Sucessfully")
   return render_template("insert_product.html")   

   
@app.route('/product_details',methods = ['POST', 'GET'])
def product_details():
   print(session)
   if session:
      if request.method == "POST":
         p_id = request.form['id']
         name = request.form['name']
         desc = request.form['desc']
         cost = request.form['cost']
         user_id = session['user_id']
         im  = request.form['im']
         data = [p_id,name,desc,cost,user_id,im]
         print(data)
         return render_template("product_details.html",data=data)
      else:
         return redirect(url_for('/'))
   else:
      return redirect(url_for('login'))

   
@app.route("/product_details_1",methods=["POST","GET"])
def product_details_1():
   if request.method == "POST":
      p_id = request.form['id']
      name = request.form['name']
      desc = request.form['desc']
      cost = request.form['cost']
      user_id = session['user_id']
      data = [p_id,name,desc,cost,user_id]
      return render_template("product_details_1.html",data=data)  

@app.route("/add_cart",methods=["POST","GET"])
def add_cart():
   if request.method == "POST":
      p_id = str(request.form['id'])
      cost = str(request.form['cost'])
      user_id = session['user_id']
      quantity = str(request.form['quantity'])
      img_path = str(request.form['img'])
      qry = "INSERT INTO `cart`( `product_id`,  `user_id`, `cost`, `quantity`) VALUES ('"+str(p_id)+"','"+str(user_id)+"','"+str(cost)+"','"+str(quantity)+"')"
      conn = mysql.connect()
      cursor = conn.cursor()
      cursor.execute(qry)
      conn.commit()

   return redirect(url_for('view_cart'))
@app.route('/place_order1',methods=["POST","GET"])
def place_order1():
   return render_template("place_order.html")
@app.route("/place_order",methods=["GET","POST"])
def place_order():
   if request.method == "POST":
      qry =  "SELECT * FROM `cart` where user_id like '"+str(session['user_id'])+"'"
      conn = mysql.connect()
      cursor = conn.cursor()
      cursor.execute(qry)
      data = cursor.fetchall()
      print("place Order")
      for row in data:
         p_id = row[1]
         cost = row[3]
         user_id = session['user_id']
         user_name = request.form['user_name']
         address = request.form['address']
         city = request.form['city']
         state = request.form['state']
         contact_no = request.form['contact_no']
         quantity = row[4]
         print("/place Order")
         print(p_id,cost,quantity,address,user_id)
         cost = int(cost) * int(quantity)
         qry = "INSERT INTO `billing_history`( `user_id`, `product_id`, `quantity`, `cost`, `address`,`user_name`,`city`,`state`,`contact_no`, `status`, `status_details`) VALUES ('"+str(user_id)+"','"+str(p_id)+"','"+str(quantity)+"','"+str(cost)+"','"+address+"','"+user_name+"','"+city+"','"+state+"','"+contact_no+"','Order Accepted','Order Processing')"
         print(qry)
         conn = mysql.connect()
         cursor = conn.cursor()
         cursor.execute(qry)
         print(qry)
         conn.commit()
      qry =  "DELETE  FROM `cart` where user_id = '"+str(session['user_id'])+"'"
      print(qry)
      conn = mysql.connect()
      cursor = conn.cursor()
      cursor.execute(qry)
      conn.commit()   
      flash("Order Placed Sucessfully")
      return redirect(url_for('product_list'))

@app.route("/view_cart",methods=["POST","GET"]) 
def view_cart():
   qry =  " SELECT * FROM `cart`,`product_details`,`user_details` "
   qry += " where cart.user_id = '"+str(session['user_id'])+"' "
   qry += " and cart.product_id = product_details.product_id "
   qry += " and cart.user_id =  user_details.user_id "
   conn = mysql.connect()
   cursor = conn.cursor()
   cursor.execute(qry)
   data = cursor.fetchall()
   total = 0
   return render_template("view_cart.html",data=data,total=total)

@app.route("/product_details_2",methods=["POST","GET"])
def product_details_2():
   if request.method == "POST":
      p_id = request.form['id']
      cost = request.form['cost']
      user_id = session['user_id']
      address = request.form['address']
      quantity = request.form['quantity']
      print("/product_details_2")
      print(p_id,cost,quantity,address,user_id)
      cost = int(cost) * int(quantity)
      qry = "INSERT INTO `billing_history`( `user_id`, `product_id`, `quantity`, `cost`, `address`, `status`, `status_details`) VALUES ('"+str(user_id)+"','"+str(p_id)+"','"+str(quantity)+"','"+str(cost)+"','"+address+"','Order Accepted','Order Processing')"
      print(qry)
      conn = mysql.connect()
      cursor = conn.cursor()
      cursor.execute(qry)
      print(qry)
      conn.commit()
      flash("Order Placed Sucessfully")
      return redirect(url_for('view_product_status'))

@app.route('/update_product_status',methods=["POST","GET"])
def update_product_status():
   qry = "SELECT * from billing_history b , product_details p  WHERE "
   qry += "b.product_id =  p.product_id and b.status <> 'Order Delivered' and b.product_id IN "
   qry += "(SELECT product_id from product_details WHERE user_id ="+str(session['user_id'])+")"
   conn = mysql.connect()
   cursor = conn.cursor()
   cursor.execute(qry)
   data = cursor.fetchall()
   conn.commit()
   return render_template("update_product_status.html",data = data)

@app.route("/update_product_status_1",methods=["POST","GET"])
def update_product_status_1():
   if request.method =="POST":
      b_id = request.form['b_id']
      s = request.form['status']
      s_r = request.form['status_r']
      qry = "UPDATE `billing_history` SET `status`='"+s+"',`status_details`='"+s_r+"' WHERE billing_id = '"+str(b_id)+"'"
      print(qry)
      conn = mysql.connect()
      cursor = conn.cursor()
      cursor.execute(qry)
      conn.commit()
      flash("Status Updated Sucessfully")
      return redirect(url_for('update_product_status'))

@app.route('/view_product_status',methods=["POST","GET"])
def view_product_status():
   print(session)
   qry = "SELECT * FROM `billing_history` WHERE user_id = "+str(session['user_id'])+""
   conn = mysql.connect()
   cursor = conn.cursor()
   print(qry)
   cursor.execute(qry)
   data = cursor.fetchall()
   print(data)
   conn.commit()
   return render_template("view_product_status.html",data = data)   
@app.route('/search',methods=["POST","GET"])
def search():
   data = []
   message = ""
   if request.method == "POST":
      txt = request.form['txt']
      qry = "SELECT * FROM `product_details` WHERE product_name LIKE '%"+txt+"%'"
      conn = mysql.connect()
      cursor = conn.cursor()
      cursor.execute(qry)
      data = cursor.fetchall()
      if  not data:
         message = "No item found"
         print(message)
      
   return render_template("search.html",data=data,message=message)


@app.route('/')
def index():
   qry =  "SELECT * FROM `product_details` "
   conn = mysql.connect()
   cursor = conn.cursor()
   cursor.execute(qry)
   data = cursor.fetchall()
   print("product_list "+str(data))
   return render_template("product_list.html",data=data)

@app.route('/sellers')
def sellers():
   qry =  "SELECT * FROM `user_details` where user_type = 'seller'"
   conn = mysql.connect()
   cursor = conn.cursor()
   cursor.execute(qry)
   data = cursor.fetchall()
   return render_template("sellers.html",data=data)


@app.route('/product_status_action',methods=["POST","GET"])
def product_status_action():
   if request.method == "POST":
      submit = request.form['submit']
      bill_no = request.form['bill_no']
      return render_template("feedback.html",data=[submit,bill_no])

@app.route('/feedback',methods=["POST","GET"])
def feedback():
   if request.method == "POST":
      feedback = request.form['feedback']
      bill_no = request.form['bill_no']
      submit = request.form['submit1']
      dat = date.today()
      if submit == 'cancel':
         qry = "DELETE FROM billing_history WHERE billing_id ='"+str(bill_no)+"'"
         conn = mysql.connect()
         cursor = conn.cursor()
         cursor.execute(qry)
         conn.commit()
         qry = "INSERT INTO cancel_history (`bill_no`,`feedback`,`user_id`,`date`) VALUES ('"+str(bill_no)+"','"+feedback+"','"+str(session['user_id'])+"','"+str(dat)+"')"
         conn = mysql.connect()
         cursor = conn.cursor()
         cursor.execute(qry)
         conn.commit()
      elif submit == 'return':
         qry = "DELETE FROM billing_history WHERE billing_id='"+str(bill_no)+"'"
         conn = mysql.connect()
         cursor = conn.cursor()
         cursor.execute(qry)
         conn.commit()
         qry = "INSERT INTO return_history (`bill_no`,`feedback`,`user_id`,`date`) VALUES ('"+str(bill_no)+"','"+feedback+"','"+str(session['user_id'])+"','"+str(dat)+"')"
         conn = mysql.connect()
         cursor = conn.cursor()
         cursor.execute(qry)
         conn.commit()
      flash(" "+submit+" request place sucessfully")
      return redirect(url_for('view_product_status'))  

@app.route('/request_approval_cancel',methods = ["POST","GET"])
def request_approval_cancel():
   
   if request.method == "POST":
      id = request.form['id']
      ap = 0
      if request.form['submit'] == "Approve":
         ap = 1
      elif request.form['submit'] == "Decline":
         ap = -1
      qry = "UPDATE `cancel_history` SET `approval`='"+str(ap)+"' WHERE id = '"+str(id)+"'"
      conn = mysql.connect()
      cursor = conn.cursor()
      cursor.execute(qry)
      conn.commit()
      flash("Response Recorded!!")
   
   qry = "SELECT * FROM cancel_history where `approval` = 0"
   conn = mysql.connect()
   cursor = conn.cursor()
   cursor.execute(qry)
   data = cursor.fetchall()
   return render_template("request_approval.html",data=["Cancel",data])

@app.route('/request_approval_return',methods = ["POST","GET"])
def request_approval_return():
   
   if request.method == "POST":
      id = request.form['id']
      ap = 0
      if request.form['submit'] == "Approve":
         ap = 1
      elif request.form['submit'] == "Decline":
         ap = -1
      qry = "UPDATE `return_history` SET `approval`='"+str(ap)+"' WHERE id = '"+str(id)+"'"
      conn = mysql.connect()
      cursor = conn.cursor()
      cursor.execute(qry)
      conn.commit()
      flash("Response Recorded!!")

   qry = "SELECT * FROM return_history  where `approval` = 0"
   conn = mysql.connect()
   cursor = conn.cursor()
   cursor.execute(qry)
   data = cursor.fetchall()
   return render_template("request_approval.html",data=["Return",data])   

@app.route('/notice',methods=["POST","GET"])
def notice():

   qry = "SELECT * FROM cancel_history WHERE user_id = '"+str(session['user_id'])+"'"
   conn = mysql.connect()
   cursor = conn.cursor()
   cursor.execute(qry)
   cancel_history = cursor.fetchall()

   qry = "SELECT * FROM return_history WHERE user_id = '"+str(session['user_id'])+"'"
   conn = mysql.connect()
   cursor = conn.cursor()
   cursor.execute(qry)
   return_history = cursor.fetchall()
   

   qry = "SELECT * FROM complaint WHERE by_user = '"+str(session['user_id'])+"'"
   conn = mysql.connect()
   cursor = conn.cursor()
   cursor.execute(qry)
   complaint = cursor.fetchall()

   return render_template("notice.html",return_history=return_history,cancel_history=cancel_history,complaint =complaint) 

@app.route('/complaint',methods=["POST","GET"])
def complaint():
   qry = "SELECT * FROM user_details WHERE user_type = 'seller' and banned = 0"
   conn = mysql.connect()
   cursor = conn.cursor()
   cursor.execute(qry)
   data = cursor.fetchall() 
   if request.method == "POST":
      user_id = request.form['user_id']
      details = request.form['complaint']
      by  = str(session['user_id'])
      qry = "INSERT INTO complaint (user_id,complaint,by_user,approval) VALUES ('"+user_id+"','"+details+"','"+by+"',0)"
      conn = mysql.connect()
      cursor = conn.cursor()
      cursor.execute(qry)  
      conn.commit()
      flash("Complaint Added")
   return render_template("complaint.html",data=data)
@app.route('/complaint_approval',methods=["POST","GET"])
def complaint_approval():
   qry = "SELECT * FROM `complaint` WHERE approval = 0"
   conn = mysql.connect()
   cursor = conn.cursor()
   cursor.execute(qry)
   data = cursor.fetchall()
   if request.method == "POST":
      id = request.form['id']
      cid = request.form['cid']
      ap = 0
      if request.form['submit'] == "Approve":
         ap = -1   
      qry = "UPDATE `user_details` SET `banned`='"+str(ap)+"' WHERE user_id = '"+str(id)+"'"
      conn = mysql.connect()
      cursor = conn.cursor()
      cursor.execute(qry)
      conn.commit()
      qry = "UPDATE `complaint` SET `approval` ='"+str(ap)+"' WHERE id ='"+str(cid)+"'"
      conn = mysql.connect()
      cursor = conn.cursor()
      cursor.execute(qry)
      conn.commit()
      flash("Response Recorded!!")
   return render_template("complaint_approval.html",data=data)

@app.route('/block',methods=["POST","GET"])
def block():
   user_id = request.args.get('user_id')
   qry = "UPDATE `user_details` set banned = 1 WHERE user_id = "+user_id
   conn = mysql.connect()
   cursor = conn.cursor()
   cursor.execute(qry)
   conn.commit()
   return redirect(url_for('sellers'))

@app.route('/unblock',methods=["POST","GET"])
def unblock():
   user_id = request.args.get('user_id')
   qry = "UPDATE `user_details` set banned = 0 WHERE user_id = "+user_id
   conn = mysql.connect()
   cursor = conn.cursor()
   cursor.execute(qry)
   conn.commit()
   return redirect(url_for('sellers'))

if __name__ == '__main__':
   app.secret_key = 'super secret key'
   app.debug = True
   app.run()      