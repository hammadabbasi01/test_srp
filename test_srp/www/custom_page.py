import frappe
from frappe import _

@frappe.whitelist(allow_guest=True)
def get_items_details():

	data = frappe.db.sql("""SELECT * FROM `tabItem` WHERE 1=1""", as_dict=True)

	return 


def get_context(context):
	data = frappe.db.sql("""SELECT * FROM `tabItem` WHERE 1=1""", as_dict=True)
	context.items = {'data': data}
	return context