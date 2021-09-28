$(document).ready(function(){
    $('.follow').click(function(event){
        event.preventDefault();
        var user_id = $(this).attr('data');

       
     $.ajax({
         url: $(this).attr('url'),
         type: 'GET',
         data: {'user_id': user_id},
         dataType: "json",
         success: function(response) {
         
             if (response.is_following){
                 $('#follow'+user_id).text('unfollow');
             }
             else {
                 $('#follow'+user_id).text('follow');
             }
     
         }
     });
    });
 });