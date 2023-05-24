import frappe
from frappe import _

from console import console


@frappe.whitelist()
def no_of_task(name):

	query = frappe.db.sql(""" 
		SELECT 
		
	    COUNT(`tabTask`.`name`) as "No. of Tasks"


		FROM  `tabProject`
		LEFT JOIN `tabTask` ON `tabProject`.`name` = `tabTask`.`project`
	  

		
		WHERE  `tabProject`.`name`='{}' """.format(name), as_list=True)


	# query = frappe.db.count('Task', {'project': name})
	db = frappe.db.set_value('Project', name , 'task_count', query[0][0])

	console("task db value").log()
	console(query).log()
	console("Project db value").log()
	console(db).log()

	try:
		return query[0][0],db
	except:
		frappe.throw("Please select the correct Project")

