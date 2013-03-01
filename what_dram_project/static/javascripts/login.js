
var mouse_is_inside = false;
$(document).ready(function() {
    
    
    $(".login_btn").mouseenter(function(){
    $("#login_box").show();
    mouse_is_inside = true;
    
    });

    $("#login_box").mouseleave(function(){
  		$("#login_box").fadeOut("slow");
  		mouse_is_inside = false;
  	});

  	
});

	

//possible soultion??? nope worse
// $(document).ready(function() {
//     var b = $('.login_btn');
//     $('#login_box').bind('mouseenter mouseleave', function(e) {    
//        var check = ( e.type === 'mouseenter' ) ?
//           ( b.stop(0).fadeIn("fast")  ) :
//           ( b.stop(0).fadeOut("slow") ) ;
//     });
// });  