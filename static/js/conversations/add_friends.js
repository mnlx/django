$(document).ready(
    function(){
        $('.btn-friends').click(
            function(){
                // var friend_id;
                // console.log(2);
                friend_id = $(this).attr("friendid");
                user_id = $(this).attr("userid");
                // console.log(friend_id);
                $.get(
                    '/conversations/add_friends/',
                    {'friend_id' : friend_id,
                    'user_id':user_id},
                    function(data){
                        $(this).html('test');
                    });

            });
        }
        );
