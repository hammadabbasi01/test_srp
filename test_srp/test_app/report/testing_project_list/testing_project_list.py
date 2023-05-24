# Copyright (c) 2023, SRP Global and contributors
# For license information, please see license.txt



import frappe
from frappe import _,msgprint
from console import console
from frappe.utils import get_url

from frappe.utils import get_link_to_form
from frappe.utils import get_url
from frappe import has_permission



def execute(filters=None):

	columns, data = [], []

	columns = get_columns()
	p_data = get_cs_data()
	g_data = get_data()
	
	if not p_data:
		msgprint('No record found')
		return columns,p_data

	
	

	for s in p_data:
		row=frappe._dict({
			'project_id' : s[0],
			'project_name' : s[1],
			'project_start_date' :s[2] ,
			'project_end_date' : s[3],
			'project_status' : s[4],
			'no_of_tasks' : s[5],
			'view_tasks' : get_data()


			})

		# wo.production_item,wo.company,
		# woi.item_name,woi.source_warehouse,woi.required_qty,woi.rate,woi.amount,woi.consumed_qty

		data.append(row)
		# for a in g_data:
		# 	# cost=0
		# 	if s[1] == "rehan":
				 
		# 		# cost+=a[7]*a[5]
		# 		row1=frappe._dict({
					
		# 			'project_id' : '',
		# 			'project_name' : '',
		# 			'project_start_date' : '' ,
		# 			'project_end_date' : '',
		# 			'project_status' : '',
		# 			'no_of_tasks' : '',
		# 			'view_tasks' : 				

		# 			})
			
		# # 	# cost_row=frappe._dict({'t_cost':cost})
			
		# # 	# data.append(cost_row)
		
		# 		data.append(row1)



	return columns,data
	
@frappe.whitelist()
def get_data():
	return {
		
		"fieldname": "project",
		"transactions": [
			{
				"label": _("Project"),
				"items": ["task"],
			},
			
		],
	}

def get_columns():
	return [

		{
			'label':_('Project ID'),
			'fieldname':'project_id',
			'fieldtype':'Link',
			'options': 'Project' ,
			'width':200
		},
		{
			'label':_('Project Name'),
			'fieldname':'project_name',
			'fieldtype':'Data',
			'width':200
		},
		{
			'label':_('Project Start Date'),
			'fieldname':'project_start_date',
			'fieldtype':'Date',
			'width':120
		},
		{
			'label':_('Project End Date'),
			'fieldname':'project_end_date',
			'fieldtype':'Date',
			'width':120
		},
		{

			'label':_('Project Status'),
			'fieldname':'project_status',
			'fieldtype':'Data',
			'width':120
		},

		{

			'label':_('No. Of Tasks'),
			'fieldname':'no_of_tasks',
			'field_type':'Data',
			'width':120
		},

		{

			'label':_('View Tasks'),
			'fieldname':'view_tasks',
			'field_type':'Link',
			'width':120
		}
	]


def get_cs_data():
	data=frappe.db.sql(
		"""
	SELECT
    `tabProject`.`name` as "Project ID:Data:120",
    `tabProject`.`project_name`  as "Project Name:Data:200",
    `tabProject`.`expected_start_date` as "Project Start Date",
    `tabProject`.`expected_end_date` as "Project End Date",
    `tabProject`.`status` as "Project Status",
    COUNT(`tabTask`.`name`) as "No. of Tasks",
    GROUP_CONCAT(CONCAT("<a href='/desk/task/view/list", `tabTask`.`name`, "' target='_blank'>", concat(concat(`tabTask`.`subject`,' - '),`tabTask`.`status`) , "</a>") SEPARATOR '  / ' ) as "Task & Status:1000"    

    FROM 
    `tabProject`
	LEFT JOIN 
	    `tabTask` ON `tabProject`.`name` = `tabTask`.`project`
	  
		GROUP BY 
	    `tabProject`.`name`
	ORDER BY 
	    COUNT(`tabTask`.`name`) DESC;
		
    


		""")
 
	
	return data




def get_data():
	# project_name = "rehan"
	# docname = "PROJ-0001"
	# doctype = "Task"
	# # filters = {"status": "Draft", "customer": "ABC Corp"}
	# form_url = get_link_to_form(doctype,docname)

	# doctype = "Task"
	# filters = {"project": "PROJ-0001"orp"}
	# list_url = get_link_to_filtered_list(doctype, filters)

	# # get the URL of the Task List form filtered by project
	# # task_list_url = frappe.utils.get_link_to_form("Task", filters={"project": "Project Name"})

	# console(form_url).log()
	# # print the URL
	# print(form_url)



	doctype = "Task"
	filters = {"project": "PROJ-0001"}
	list_url = get_url("/desk#List/{0}?filters={1}".format(doctype, filters))
	console(list_url).log()
	return list_url


    # data = {
    #     "fieldname": "project",
    #     "transactions": [
    #         {
    #             "label": _("Tasks"),
    #             "items": ["Task"
    #                 # {
    #                 #     "type": "doctype",
    #                 #     "name": "Task",
    #                 #     "label": _("All Tasks"),
    #                 #     "description": _("All Tasks linked to the Project"),
    #                 #     "filters": {
    #                 #         "project": "project_name"
    #                 #     }
    #                 # }
    #             ]
    #         }
    #     ]
    # }
    # console("rehan").log()
    # console(data["transactions"]).log()
    # console(data['transactions'][0]).log()
    
    



