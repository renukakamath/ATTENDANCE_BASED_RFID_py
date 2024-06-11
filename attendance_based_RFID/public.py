from flask import Blueprint,render_template,request,redirect,url_for,session,flash 
import uuid
from database import*




public=Blueprint('public',__name__)


@public.route('/')
def home():
	return render_template('public_home.html')

@public.route('/employee_register',methods=['post','get'])	
def employee_register():
	if "employee" in request.form:
		f=request.form['fname']
		l=request.form['lname']
		p=request.form['place']
		ph=request.form['phone']
		e=request.form['email']
		c=request.form['card']
		i=request.files['img']
		u=request.form['uname']
		pw=request.form['pwd']
		path="static/image/"+str(uuid.uuid4())+i.filename
		i.save(path)
		q="select * from login where username='%s' and password='%s'"%(u,pw)
		res=select(q)
		if res:
			flash('already exist')

		else:
			q="insert into login values(null,'%s','%s','pending')"%(u,pw)
			id=insert(q)
			q="insert into employee values(null,'%s','%s','%s','%s','%s','%s','pending','pending','%s','%s')"%(id,f,l,p,ph,e,c,path)
			insert(q)
			flash('inserted successfully')
			return redirect(url_for('public.employee_register'))
		
	return render_template('employee_register.html')

@public.route('/login',methods=['post','get'])	
def login():
	if "login" in request.form:
		u=request.form['uname']
		pw=request.form['pwd']
		q="select * from login where username='%s' and password='%s'"%(u,pw)
		res=select(q)
		if res:
			session['login_id']=res[0]['login_id']
			lid=session['login_id']
			if res[0]['usertype']=="admin":
				return redirect(url_for('admin.admin_home'))

			elif res[0]['usertype']=="employee":
				q="select * from employee where login_id='%s'"%(lid)
				res=select(q)
				if res:
					session['employee_id']=res[0]['employee_id']
					eid=session['employee_id']
				return redirect(url_for('employee.employee_home'))

	else:
		flash('invalid username and password')
				
			

		
	return render_template('login.html')
	


	


	


