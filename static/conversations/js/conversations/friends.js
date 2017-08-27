$(document).ready(
    function(){
        $('.btn-friends').click(
            function(){
                friend_id = $(this).attr("friendid");
                user_id = $(this).attr("userid");

                $.get(
                    '/conversations/ajax/add_friends/',
                    {'friend_id' : friend_id,
                    'user_id':user_id},
                    function(data){
                        $(this).html('test');
                    });

            });

        $('.btn-not-friends').click(
            function(){

                friend_id = $(this).attr("friendid");
                user_id = $(this).attr("userid");

                $.get(
                    '/conversations/ajax/add_friends/',
                    {'friend_id' : friend_id,
                    'user_id':user_id},
                    function(data){
                        $(this).html('test');
                    });

            });
        });
