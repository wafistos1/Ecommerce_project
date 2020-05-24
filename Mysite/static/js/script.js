
// $(document).ready(function(event){

//     $('.reply-btn').click(function(){
//         $(this).parent().parent().next('.replies-comments').fadeToggel()
//     });

// });

$(document).on('submit', '.comment-from', function (event) {

    event.preventDefault();

    $.ajax({
        type: 'POST',
        url: $(this).attr('action'),
        data: $(this).serialize(),
        dataType: 'json',
        success: function(response){
            $('.main-comment-section').html(response['form']);
            $('textarea').val('');

            $('.reply-btn').on('click', function () {
                $(this).parent().parent().next('.replies-comments').fadeToggle();
                $('textarea').val('');

            });

        },
        error: function (rs, e) {
            console.log(rs.responseText);
        }
    });

});


$(document).on('submit', '.reply-form', function (event) {

    event.preventDefault();

    $.ajax({
        type: 'POST',
        url: $(this).attr('action'),
        data: $(this).serialize(),
        dataType: 'json',
        success: function(response){
            $('.main-comment-section').html(response['form']);
            $('textarea').val('');

            $('.reply-btn').on('click', function(){
            $(this).parent().parent().next('.replies-comments').fadeToggle();

            $('textarea').val('');
                });


        },
        error: function (rs, e) {
            console.log(rs);
        }
    });

});

$('.reply-btn').on('click', function(){
    $(this).parent().parent().next('.replies-comments').fadeToggle();

    
        });

$('#btn-commentaires').on('click', function(){
    $('#commentaires').fadeToggle();
    
        });


        $(function () {
            $("#mdb-lightbox-ui").load("mdb-addons/mdb-lightbox-ui.html");
           });

$('#btn-advanced-search').on('click', function(){
$('#advanced-search').fadeToggle();

    });

