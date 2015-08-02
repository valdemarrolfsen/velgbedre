var addProduct;
var saveWishlist;
var getCookie;
var selectedInfobox;

$(document).ready(function() {

	addProduct = function() {
		var productId = $('#product' + selectedProduct).data("productid");
		var index = $.inArray(productId, wishlist);

		if (index < 0)
			wishlist.push(productId);
		else
			wishlist.splice(index, 1);
	}

	toggleSelectButton = function(button) {
		var productId = $('#product' + selectedProduct).data("productid");

		var isInList = ($.inArray(productId, wishlist)>=0);

		console.log(isInList);

		if (isInList && !button.hasClass('selected')) {
			button.addClass('selected');
			button.html("<span class='glyphicon glyphicon-ok' aria-hidden='true'></span><p>Produkt lagt til</p>");
		} else if (!isInList) {
			button.removeClass('selected');
			button.html("<span class='glyphicon glyphicon-heart' aria-hidden='true'></span><p>Legg til i Ønskeliste</p>");
		}
	}

	saveWishlist = function(list) {

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
			url: 'frontpage',
			data: {	
				'data': JSON.stringify({wishlist : list}, null, 2)
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
})

$('#add-product').click( function() {
	addProduct();
	toggleSelectButton($('#add-product'));
	console.log(wishlist);
	saveWishlist(wishlist)
	$('#go-to-wishlist').fadeIn();
});

$('#go-to-wishlist').click(function() {
	window.location.replace("/company/wishlist");
});

$('.picture').click(function() {
	var picture = $(this).data('picture');
	$('#picture-slider' + selectedProduct).fadeIn();
	$('#picture-carousel' + selectedProduct + ' .carousel-inner .picture' + picture).addClass('active');
})

$('.close').click(function() {
	$('#picture-slider' + selectedProduct).fadeOut();
	$('#picture-carousel' + selectedProduct + ' .carousel-inner .item').removeClass('active');
})

$('#carousel-left').click(function() {

	selectedType = -1;

	$('#product' + selectedProduct).fadeOut();

	if (selectedProduct <= 0)
		selectedProduct = numProducts-1;
	else
		selectedProduct -= 1;

	toggleSelectButton($('#add-product'));

	$('#product' + selectedProduct).fadeIn();
})

$('#carousel-right').click(function() {
	selectedType = -1;
	
	$('#product' + selectedProduct).fadeOut();

	if (selectedProduct < numProducts-1)
		selectedProduct += 1;
	else
		selectedProduct = 0;

	toggleSelectButton($('#add-product'));

	$('#product' + selectedProduct).fadeIn();
})

$('#carousel-indicators li').click(function() {
	$('#product' + selectedProduct).fadeOut();

	selectedProduct = $(this).data("slide-to");

	toggleSelectButton($('#add-product'));

	$('#product' + selectedProduct).fadeIn();
})

$('#intro-close').click(function() {
	$('#intro-message').fadeOut();
})

$('#intro-message').click(function(e) {
	if (e.target == this)
		$('#intro-message').fadeOut();
})

// ------------- Product types -------------
$('#productTypes').change(function() {
	selectedType = $('#productTypes option:selected').data("type");

	console.log($('#productTypes option:selected').data("type"));
});

// ------------- Infoboxes ---------------
$('#first-icon').click(function() {
	var pos = $(this).offset();

	if (selectedInfobox == 1) {
		$('.infobox').fadeOut();
		$('.pointer').hide();
		selectedInfobox = 0;

		return
	}

	selectedInfobox = 1;

	$('.infobox').css({'top':pos.top - 500});
	$('.pointer').css({'left':pos.left + 50});

	$('.infobox').fadeIn();
	$('.pointer').show();

});

$('#second-icon').click(function() {
	var pos = $(this).offset();

	if (selectedInfobox == 2) {
		$('.infobox').fadeOut();
		$('.pointer').hide();
		selectedInfobox = 0;
		return
	}

	selectedInfobox = 2;

	$('.infobox').css({'top':pos.top - 500});
	$('.pointer').css({'left':pos.left + 50});

	$('.pointer').show();
	$('.infobox').fadeIn();
});

$('#third-icon').click(function() {
	var pos = $(this).offset();

	if (selectedInfobox == 3) {
		$('.infobox').fadeOut();
		$('.pointer').hide();
		selectedInfobox = 0;
		return
	}

	selectedInfobox = 3;

	$('.infobox').css({'top':pos.top - 500});
	$('.pointer').css({'left':pos.left + 50});

	$('.infobox').fadeIn();
	$('.pointer').show();

});