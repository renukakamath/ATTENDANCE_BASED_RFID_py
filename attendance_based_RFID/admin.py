from flask import Blueprint,render_template,request,redirect,url_for,flash
from database import*

admin=Blueprint('admin',__name__)

@admin.route('/admin_home')
def admin_home():
	return render_template('admin_home.html')

@admin.route('/admin_viewemployee')
def admin_viewemployee():
	data={}
	q="select * from employee inner join login using (login_id)"
	res=select(q)
	data['emp']=res

	if "action" in request.args:
		action=request.args['action']
		lid=request.args['lid']

	else:action=None


	if action=='accept':
		q="update login set usertype='employee' where login_id='%s'"%(lid)
		update(q)
		q="update employee set status='accept' where login_id='%s'"%(lid)
		update(q)
		flash(' successfully')
		return redirect(url_for('admin.admin_viewemployee'))

	if action=='reject':
		q="update login set usertype='block' where login_id='%s'"%(lid)
		update(q)
		q="update employee set status='reject' where login_id='%s'"%(lid)
		update(q)
		flash(' successfully')
		return redirect(url_for('admin.admin_viewemployee'))


	if "act" in request.args:
		act=request.args['act']
		eid=request.args['eid']

	else:act=None

	if act=='provide':
		q="update  employee set cardstatus='Provide Card' where employee_id='%s'"%(eid)
		update(q)
		flash(' successfully')
		return redirect(url_for('admin.admin_viewemployee'))

	if act=='remove':
		q="delete from employee where employee_id='%s'"%(eid)
		delete(q)
		flash(' successfully')
		return redirect(url_for('admin.admin_viewemployee'))

	return render_template('admin_viewemployee.html',data=data)

@admin.route('admin_viewattendance')	
def admin_viewattendance():
	data={}
	eid=request.args['eid']
	q="select * from attendance inner join employee using (employee_id) where employee_id='%s'"%(eid)
	res=select(q)
	data['att']=res

	return render_template('admin_viewattendance.html',data=data)