

$(document).ready(function() {
    
    
    $(".login_btn").hover(function(){
    $("#login_box").fadeIn("fast");
    return true;
    },
    function(){
        $("#login_box").fadeOut("slow");
        return false;
    });
});  