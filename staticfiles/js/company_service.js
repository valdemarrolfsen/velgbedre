var addProduct;
var getCookie;
var selectedProduct;
var selectedType;

$(document).ready(function() {

	selectedProduct = 0;

	selectedType = $('#productTypes' + selectedProduct + ' option:selected').val();

	$('#picture-slider0').hide();
	$('#do-post').hide();
	$('.infobox').hide();
	$('.pointer').hide();

	$('.product-picture').hide();

	$('#product-picture' + selectedType).show();

	console.log(wishlist);

	for (var i = 1; i<numProducts; i++) {
		$('#picture-slider' + i).hide();
		$('#product' + i).hide();
	}

	toggleSelectButton($('.add-product'));

	// ------------- Product types -------------
	$('.productTypes').change(function() {
		$('#product-picture' + selectedType).fadeOut();

		selectedType = $('#productTypes' + selectedProduct + ' option:selected').val();

		$('#product-picture' + selectedType).fadeIn();

		if ($('.add-product').hasClass('selected')) {
			$('.add-product').removeClass('selected');
			$('.add-product').addClass('updateble');
			$('.add-product').html("<span class='glyphicon glyphicon-heart' aria-hidden='true'></span><p>Oppdater ønskeliste</p>");
		}
	});
})

toggleSelectButton = function(button) {
	var productId = $('#product' + selectedProduct).data("productid");

	var isInList = false;

	wishlist.forEach(function(entry) {
		if (productId==entry.product) {
			isInList = true;
			selectedType = entry.type;
		}
	});

	$('#productTypes' + selectedProduct).val(selectedType);

	if (isInList && !button.hasClass('selected')) {
		button.addClass('selected');
		button.removeClass('updateble');
		button.html("<span class='glyphicon glyphicon-ok' aria-hidden='true'></span><p>Produkt lagt til</p>");
	} else if (!isInList) {
		button.removeClass('selected');
		button.removeClass('updateble');
		button.html("<span class='glyphicon glyphicon-heart' aria-hidden='true'></span><p>Legg til i Ønskeliste</p>");
	}
}

pushProduct = function() {

	var productId = $('#product' + selectedProduct).data("productid");

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
			'productId' : productId,
			'typeId' : selectedType
		},
		success: function(response) {
			if (response=='delete') {
				var index;

				wishlist.forEach(function(entry, i) {
					if (productId==entry.product) {
						index = i;
					}
				});

				wishlist.splice(index, 1);

			} else if (response=='new')
				wishlist.push({'product' : productId, 'type' : selectedType});
			else {
				wishlist.forEach(function(entry) { 
					if (entry.product == productId)
						entry.type = selectedType
				});
			}

			swal({   
				title: "Ønskeliste lagret!",
				type: "success",
				timer: 1500,
				showConfirmButton: false 
			});

			toggleSelectButton($('.add-product'));
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

$('.add-product').click( function() {
	pushProduct();
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

	$('#product' + selectedProduct).fadeOut();

	if (selectedProduct <= 0)
		selectedProduct = numProducts-1;
	else
		selectedProduct -= 1;

	toggleSelectButton($('.add-product'));

	$('#product' + selectedProduct).fadeIn();

	$('#product-picture' + selectedType).hide();

	selectedType = $('#productTypes' + selectedProduct + ' option:selected').val();

	$('#product-picture' + selectedType).fadeIn();
})

$('#carousel-right').click(function() {
	
	$('#product' + selectedProduct).fadeOut();

	if (selectedProduct < numProducts-1)
		selectedProduct += 1;
	else
		selectedProduct = 0;

	toggleSelectButton($('.add-product'));

	$('#product' + selectedProduct).fadeIn();

	$('#product-picture' + selectedType).hide();

	selectedType = $('#productTypes' + selectedProduct + ' option:selected').val();
	
	$('#product-picture' + selectedType).fadeIn();
})

$('#carousel-indicators li').click(function() {
	$('#product' + selectedProduct).fadeOut();

	selectedProduct = $(this).data("slide-to");

	$('#product-picture' + selectedType).fadeOut();

	selectedType = $('#productTypes' + selectedProduct + ' option:selected').val();

	$('#product-picture' + selectedType).fadeIn();

	toggleSelectButton($('.add-product'));

	$('#product' + selectedProduct).fadeIn();
})

// --------------- Intro message ---------------

$('#intro-close').click(function() {
	$('#intro-message').fadeOut();
})

$('#intro-message').click(function(e) {
	if (e.target == this)
		$('#intro-message').fadeOut();
})