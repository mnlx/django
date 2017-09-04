$(document).ready(
    function() {
        $('select').material_select();

        // $('.friends-container li').click(
        //     function(){
        //
        //         a = $(this).children()[0].value;
        //         console.log(a);
        //         $('input#friend_id')[0].value = a;
        //     });

        // $.get(
        //     '/conversations/remove_friends/',
        //     {'user_id':user_id},
        //     function(data){
        //         $(this).html('test');
        //     });



    $('.friend-bar').click(
        function () {
            $('.active').removeClass('active')
            $(this).addClass('active')
            // console.log(2);
            // a = $(this).children()
            friend_id = $(this).children()[0].value;
            // console.log(friend_id)
            $.get({
                    url: '/conversations/ajax/get_messages',
                    data : {'friend_id':friend_id},
                    success : function (data) {
                    console.log(2)
                    console.log(data)
                    a = data;
                    msg = $('.text-container')
                    for (i=0;i<msg.length;i++){
                        // console.log(msg)
                        if(data[i]) {
                            console.log(1)
                            $(msg[i]).html(data[i]);
                            $($('.text-container')[i]).parent().parent().parent().slideDown();
                        }

                        else {
                            console.log($(this).parent().parent().parent())
                            $($('.text-container')[i]).parent().parent().parent().slideUp();
                        }
                        }


                    }
                }
            )

        }


    )
});