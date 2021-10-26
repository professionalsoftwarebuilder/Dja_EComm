//alert('begin main');

/// Selecteer alle thumbnails

var theThumbs = document.querySelectorAll('.zi-small-img');
// / Set the borders

const fncCleanThumbs = () => {
	theThumbs.forEach(aThumb => aThumb.style.border = 'none');
};

//$('#zi-show-img').queue(fx)


// /$('.zi-small-img:first-of-type').css({border: 'solid 1px #951b25', padding:
// '2px'})
// /$('.zi-small-img:first-of-type').attr('alt',
// 'now').siblings().removeAttr('alt')

// / Wanneer op de thumbnail wordt geclicked
$('.zi-small-img').click(function () {

	/// Verwijder de border van de vorige thumb
	fncCleanThumbs();
	
	/// Zet de border van de geklikte thumb
	$(this).css({border: 'solid 3px blue' });

	//$('#zi-show-img').clearQueue(fx);
	
	//alert('hallo');
	//dequeue('zoomImage');
	// / Stop url van thumbnail in active (schouw image)
    $('#zi-show-img').attr('src', $(this).attr('src'))  // Note: $(this).width() will not work for in memory images

    //$('#zi-show-img').zoomImage();
    
  // / Haal breedte en hoogte op
  var theHeight = $('#zi-show-img').height();
  var theWidth = $('#zi-show-img').width();

  // / Stop url van thumbnail in vergrootglas image (het onthefly image)
  $('#big-img').attr('src', $(this).attr('src'))
  $('#big-img').height(theHeight * 5);
  $('#big-img').width(theWidth * 5);

  
  //$('#pietjepuk').height(theHeight);
  //$('#pietjepuk').width(theWidth);
//   $('.zi-show').height(theHeight);
//  $('.zi-show').width(theWidth);
})

