$(document).ready(function(){

$('.answer').hide();


$('a.close').on('click',function(c){
	
	var parentDiv = $(this).parent();
	parentDiv.fadeOut('fast');
	c.preventDefault();
});

$('a.button').on('click',function(c){
	
	$(this).next('div.content.answer').fadeIn('fast');
	c.preventDefault();
});


});