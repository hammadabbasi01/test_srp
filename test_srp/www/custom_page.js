$(document).ready(function(){
	frappe.call({
	    method: 'test_srp.www.custom_page.get_items_details',
	    args: {
	    },
	    // freeze the screen until the request is completed
	    freeze: true,
	    callback: (r) => {
	        // on success
	        if (r.message){
	        	console.log(r.message)
	        	$("#page-content").val(r.message)
	        }
	    },
	    error: (r) => {
	        // on error
	        console.log('some error in getting items details!')
	    }
	});
})
$(document.body).css('backrgound-colr', 'gray')