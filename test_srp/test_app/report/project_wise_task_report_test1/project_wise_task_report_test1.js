// Copyright (c) 2023, SRP Global and contributors
// For license information, please see license.txt
/* eslint-disable */


// frappe.query_reports["Project wise Task Report test1"] = {
// 	"filters": [

// 	]
// };


// frappe.query_reports["Project wise Task Report test1"] = {
//     "filters": [
//         {
//             "fieldname":"project",
//             "label": __("Project"),
//             "fieldtype": "Link",
//             "options": "Project"
//         }
//     ],

//     "formatter": function(value, row, column, data, default_formatter) {
//         if (column.fieldname == "total_task_count") {
//             return data.total_task_count || 0;
//         }
//         else {
//             return default_formatter(value, row, column, data);
//         }
//     },

//     "onload": function(report) {
//         report.page.add_inner_button(__("Refresh"), function() {
//             report.refresh();
//         });
//     },

//     "refresh": function(report) {
//         frappe.call({
//             method: "test_app.report.project_wise_task_report_test1.get_data",
//             args: {
//                 project: report.filters_by_name.project.get_value()
//             },
//             callback: function(data) {
//                 report.data = data.message;
//                 report.refresh();
//             }
//         });
//     }
// };

// frappe.query_reports["Project wise Task Report test1"] = {
// 	"filters": [
// 		{
// 			"fieldname": "project",
// 			"label": __("Project"),
// 			"fieldtype": "Link",
// 			"options": "Project"
// 		}
// 	],

// 	"onload": function(report) {
// 		report.page.add_inner_button(__("Refresh"), function() {
// 			report.run();
// 		});
// 	},

// 	"formatter": function(row, cell, value, columnDef, dataContext, default_formatter) {
// 		if (columnDef.id == "task") {
// 			value = "<a href='#Form/Task/" + dataContext.task + "'>" + value + "</a>";
// 		}
// 		return default_formatter(row, cell, value, columnDef, dataContext);
// 	},

// 	"get_datatable_options": function() {
// 		var project = frappe.query_report.filters_by_name.project.get_value();
// 		return {
// 			columns: [
// 				{ id: "task", name: __("Task"), field: "task", width: 200 },
// 				{ id: "description", name: __("Description"), field: "description", width: 200 },
// 				{ id: "status", name: __("Status"), field: "status", width: 100 },
// 				{ id: "priority", name: __("Priority"), field: "priority", width: 100 }
// 			],
// 			get_data: function() {
// 				return frappe.call({
// 					method: "test_srp.test_app.report.project_wise_task_report_test1.get_data",
// 					args: { project: project },
// 					callback: function(response) {
// 						var data = response.message;
// 						$.each(data, function(i, d) {
// 							d.id = i + 1;
// 						});
// 						return data;
// 					}
// 				});
// 			}
// 		};
// 	}
// };
