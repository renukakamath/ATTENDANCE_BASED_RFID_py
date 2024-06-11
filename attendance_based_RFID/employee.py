from flask import Blueprint,render_template,session 
from database import*


employee=Blueprint('employee',__name__)


@employee.route('/employee_home')
def employee_home():
	return render_template('employee_home.html')

@employee.route('/employee_viewprofile')
def employee_viewprofile():
	data={}
	eid=session['employee_id']
	q="select * from employee where employee_id='%s'"%(eid)
	res=select(q)
	data['emp']=res
	return render_template('employee_viewprofile.html',data=data)
@employee.route('/employee_viewattendance')
def employee_viewattendance():
	eid=session['employee_id']
	data={}
	q="select * from attendance inner join employee using (employee_id) where employee_id='%s'"%(eid)
	res=select(q)
	data['att']=res
	return render_template('employee_viewattendance.html',data=data)

	