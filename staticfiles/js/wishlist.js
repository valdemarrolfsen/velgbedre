$(document).ready(function() {

	$( "#sortable" ).sortable({
		revert: true,
		change: function( event, ui ) {
			$('#save-wishlist').fadeIn();
			$('#close-window').fadeOut();
		}
	});
	$( "#sortable" ).disableSelection();

	$('#close-window').hide();

	$('#save-wishlist').click(function() {
		var sortedIDs = $("#sortable").sortable("toArray");
		pushWishlist(sortedIDs);
		$(this).fadeOut();
		$('#close-window').fadeIn();
	});

	$('#close-window').click(function() {
		swal({
			title: "Er du sikker?",
			text: "Ved å gå videre vil du avslutte gavevelgeren",
			type: "warning",
			showCancelButton: true,
			confirmButtonText: "Lukk vindu",
			cancelButtonText: "Gå tilbake",
			closeOnConfirm: false,
			closeOnCancel: false },
			function(isConfirm){
				if (isConfirm) {
					window.location.replace("http://www.velgbedre.no");
				} else {
					swal({   
						title: "Avbrutt",
						type: "error",
						timer: 1500,
						showConfirmButton: false 
					});
				}
			});
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
				title: "Ønskeliste lagret!",
				type: "success",
				timer: 1500,
				showConfirmButton: false 
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