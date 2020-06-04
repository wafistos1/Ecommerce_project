
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

$('.btn-search').on('click', function (e) {
    e.preventDefault();
    
    var categories = $('#categories').val();
	var type_annonce = $('#type_annonce').val();
	var date_gt = $('#date_gt').val();
	var date = $('#date').val();
	var date_lt = $('#date_lt').val();
	var price = $('#price').val();
	var price_gt = $('#price_gt').val();
    var price_lt = $('#price_lt').val();
    $('.add-filter').children().remove();
    $('.pagination').children().remove();
	// alert( 'rating: ' + rating + ' grade: ' + grade+ ' categorie: ' + categorie );

	$.ajax({
		url: "/search/filter/",
		type: 'GET',

		data: {
			csrfmiddlewaretoken: '{{ csrf_token }}',
			'categories': categories,
			'type_annonce': type_annonce,
			'date_gt': date_gt,
			'date_lt': date_lt,
			'date': date,
			'price': price,
			'price_gt': price_gt,
			'price_lt': price_lt,
        },
        datatype:'json',
		success: function (response, status) {
            
            $('.add-filter').html(response['form']);

			
				

		},
		error: function (data) {
			alert("ajax call failed!");
		}
	});


    
});