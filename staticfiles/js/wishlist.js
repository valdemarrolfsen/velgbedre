$(document).ready(function() {

	$( "#sortable" ).sortable({
		revert: true
	});
	$( "#sortable" ).disableSelection();

	$('#send-wishlist').click(function() {
		var sortedIDs = $("#sortable").sortable("toArray");
		pushWishlist(sortedIDs);
	});
});

// ------------- functions -----------------
pushWishlist = function(wishlist) {

	//Add csrf-token 
	$.ajaxSetup({
	    beforeSend: function(xhr, settings) {
	        if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
	            // Only send the token to relative URLs i.e. locally.
	            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
	        }
	    }
	});

	//[TODO] Should get url from django template tag
	$.ajax({
		type: 'POST',
		url: 'wishlist',
		data: {	
			'wishlist' : JSON.stringify(wishlist, null, 2)
		},
		success: function() {
			swal({
			title: "Er du sikker?",
			text: "Ved å trykke send inn, vil du bli ført bort fra denne siden",
			type: "warning",
			showCancelButton: true,
			confirmButtonText: "Send inn",
			cancelButtonText: "Gå tilbake",
			closeOnConfirm: false,
			closeOnCancel: false },
			function(isConfirm){
				if (isConfirm) {
					swal({   
						title: "Ønskeliste sendt inn!",
						type: "success",
						timer: 2500,
						showConfirmButton: false 
					});
					setTimeout(function() {window.location.replace("http://www.velgbedre.no");}, 2500)
				} else {
					swal({   
						title: "Avbrutt",
						type: "error",
						timer: 1500,
						showConfirmButton: false 
					});
				}
			});
		}

	});
}

getCookie = function(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}