$(document).ready(function(){
    $('.like').click(function(event){
        event.preventDefault();
        var post_id = $(this).attr('data');
        var like_url = $(this).attr('url');
        
        $.ajax({
        type: "GET",
        url: like_url,
        data: {'post_id': post_id},
        dataType: "json",
        success: function(response) {
                                               
            if (response.is_liked){
                $('#like'+post_id).text('liked');
            }
            else {
                $('#like'+post_id).text('like');
            }
           
            $('#count'+post_id).text(response.total_likes);
           }
            
        });
        });
    });
