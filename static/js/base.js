$(function(){
	$('.btn').tooltip({ placement: 'bottom'})

	$('#hidenav').on('click',function(e){
		e.preventDefault();
		var na = $('nav');

		if(na.css('display') === 'block')
			na.hide();
		else
			na.show();
	})

	$('.expand').on('click', function(e){
		e.preventDefault();

		var parent = $(this).parent('li');
		var child = parent.children('ul');
		
		if(child.hasClass('expanded') || parent.hasClass('active')){
			child.removeClass('expanded').slideUp()
			return;
		}

		if($('.expanded').size() > 0){
			$('.expanded').removeClass('expanded').slideUp()
		}
		child.slideDown().addClass('expanded');
	})

	$('#subnav').perfectScrollbar()
})