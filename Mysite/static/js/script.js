
// $(document).ready(function(event){

//     $('.reply-btn').click(function(){
//         $(this).parent().parent().next('.replies-comments').fadeToggel()
//     });

// });

$fadeRating = $('.reply-btn');
$fadeRating.on('click', function () {
    $(this).parent().parent().next('.replies-comments').fadeToggle();

});