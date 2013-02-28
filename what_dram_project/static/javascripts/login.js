

$(document).ready(function() {
    
    
    $(".login_btn, #login_box").hover(function(){
    $("#login_box").show("fast");
    },
    function(){
        $("#login_box").fadeOut("slow");
    });
});  