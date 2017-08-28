$(document).ready(
    function(){
        $('.btn-friends').click(
            function(){
                friend_id = $(this).parent().parent().find('#friend-id').value;

                $.get(
                    "{% url 'ajax:add_friends' %}",

                    {'friend_id' : friend_id,
                            'user_id':user_id},
                            function(data){
                                $(this).html('test');
                            });
                console.log('added');

            });

        $('.btn-not-friends').click(
            function(){
                console.log('removed');
                friend_id = $(this).parent().children('#friend-id')[0].value;
                // user_id = $(this).attr("userid");
                console.log(friend_id);
                $.get(
                    '/conversations/ajax/remove_friends',
                    {'friend_id' : friend_id,
                    },
                    function(data){
                        $(this).html('test');
                    });
                console.log('removed3');

            });
        });
