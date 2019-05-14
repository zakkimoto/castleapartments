<<<<<<< HEAD
=======


>>>>>>> d3587292ca16d658bf722fb24e8410c38a6ac896
$(document).ready(function(){
    $('.search-btn').on('click', function(e) {
        e.preventDefault();
        var searchText = $('.search-box').val();
        $.ajax({
            url: '/properties?search_filter=' + searchText,
            type: 'GET',
            success: function(resp){
                var newHTML = resp.data.map(d => {
                    return `<div class="well property">
                                <a href="/properties/${d.id}">
                                    <img class="property-img" src="${d.firstImage}"/>
                                    <h4>${d.streetname}</h4>
                                    <p>${d.description}</p>
                                </a>
                               </div>`
                });
                $('.properties').html(newHTML.join(''));
                $('.search-box').val('');

            },
            error: function(xhr, status, error){
                console.error(error)
            }
        })
    });

});



