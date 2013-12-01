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

	$('select').selectric()

	$('.expand').on('click', function(e){
		e.preventDefault();

		var parent = $(this).parent('li');
		var child = parent.children('ul');
		
		if(child.hasClass('expanded') ){
			child.removeClass('expanded').slideUp()
			return;
		}

		if($('.expanded').size() > 0){
			$('.expanded').removeClass('expanded').slideUp()
		}
		child.slideDown().addClass('expanded');
	})

	//Registrar alumnos
	$('.registry_c').on('click',function(e){
		e.preventDefault();
		var self = $(this);
		var icon = '<i class="glyphicon glyphicon-download-alt"></i>';
		var spinner = '<div class="progress small"></div>'
		$.ajax({
			type: 'POST',
			url: '/inscripcion/inscribir/',
			data: {clase: self.data('clase'), 'csrfmiddlewaretoken': $('meta[name=csrf_token]').attr('content')},
			beforeSend: function(){
				self.attr('disabled', 'disabled').html(spinner);
			},
			error: function(jx,h,b){
				console.log(b)
				self.removeAttr('disabled').html(icon);
				alertify.error('No se pudo inscribir <strong>'+self.data('nnombre')+'</strong>.  Vuelve a intentar');
			},
			success:function(data){
				if(data.status === 0){
					self.removeAttr('disabled').html(icon);
					alertify.error('No se pudo inscribir <strong>'+self.data('nnombre')+'</strong>. '+data.error+' - Vuelve a intentar');
				}else if(data.status === 1){
					var parent = self.parent('td').parent('tr');
					alertify.success('Se inscribio la materia: <strong>'+self.data('nnombre')+'</strong>')
					parent.slideUp('slow',function(){
						parent.remove();
					})
				}
			}
		})
	})

	$('#id_fecha_nacimiento').datepicker({format: 'dd/mm/yyyy'});
	$('.timeI').timepicker({
		minuteStep: 30,
		showMeridian: false
	});
})