/*
var mouse_is_inside = false;

$(document).ready(function() {
    $(".login_btn").click(function() {
        var loginBox = $("#login_box");
        if (loginBox.is(":visible"))
            loginBox.fadeOut("fast");
        else
            loginBox.fadeIn("fast");
        return false;
    });
    
    $("#login_box").hover(function(){ 
        mouse_is_inside=true; 
    }, function(){ 
        mouse_is_inside=false; 
    });

    $("body").click(function(){
        if(! mouse_is_inside) $("#login_box").fadeOut("fast");
    });
});
*/

$(document).ready(function() {
    
    
    $(".login_btn, #login_box").hover(function(){
    $("#login_box").fadeIn("fast");
    return true;
    },
    function(){
        $("#login_box").fadeOut("slow");
        return false;
    }); 