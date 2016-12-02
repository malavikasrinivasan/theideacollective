$(document).ready(
    $("#comment-btn").on('click', function() {
        
        var comment =  $("#comment").val(); // Get value from the form
        var idea_id = $("#newcomment").attr("name");
        var idea_owner = $('#idea-owner').text();
        // alert(idea_id);
        // alert($('#idea-owner').text());

        var comment_html = '<li class="collection-item avatar"><img src="../static/nancy.jpg" alt="" class="circle"><span class="title">'+idea_owner+'</span><p>'+comment+'</p></li>';
        $('#comment-container').append(comment_html); //Append comment to DOM

        // Ajax call to write comment to the database

        $.ajax({
          url: '/addcomment',
          type: 'POST',
          data: { data:
            JSON.stringify({
              "comment": comment,
              // "user_id": <>,
              "idea_id": idea_id,
              // "ts": <current_ts>
            })
          },
          success: function() {
              
          }
        });



        $("#comment").val(""); // Clear the form
      
        
    })
);

