
var mouse_is_inside = false;
$(document).ready(function() {
    
    
    $(".login_btn, #login_box").mouseenter(function(){
    $("#login_box").show();
    mouse_is_inside = true;
    
    });

    $(".login_btn, #login_box").mouseleave(function(){
  		$("#login_box").hide();
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