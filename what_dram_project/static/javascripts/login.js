

$(document).ready(function() {
    
    
    $(".login_btn, #login_box").hover(function(){
    $("#login_box").fadeIn("fast");
    },
    function(){
        $("#login_box").fadeOut("slow");
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