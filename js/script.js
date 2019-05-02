$(function() {
    console.log( "ready!" );
    $(".close_but").click
    (
        function(){
            $(this).parent().parent().remove();
        }
    );
    $(".notice_close").click
    (
        function(){
            $(this).parent().parent().remove();
        }
    );
});//END