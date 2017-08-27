$(document).ready(function() {
$('select').material_select();

$('.friends-container li').click( function(){

    a = $(this).children()[0].value;
    console.log(a);
    $('input#friend_id')[0].value = a;
});

        $.get(
            '/conversations/remove_friends/',
            {'user_id':user_id},
            function(data){
                $(this).html('test');
            });




});