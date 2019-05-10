$(document).ready(function(){
    $('#search-btn').on('click', function(e){
        e.preventDefault();
        var searchText = $('#search-box').val();
        $.ajax({
            url: '/properties/?search_filter=' + searchText,
            type: 'GET',
            success: function(resp) {
                var newHtml = resp.data.map(d => {
                    return `<div class="well property">
                                <a href="/properties/${d.id}">
                                    <img class="property-img" src="${d.firstImage}"/>
                                    <h4>${d.streetname}</h4>
                                    <p>${d.description}</p>
                                </a>
                            </div>`
                });
                $('.properties').html(newHtml.join(''));
                $('#search-box').val('');
            },
            error: function (xhr, status, error) {
                // TODO: Show toastr
                console.error(error)
            }
        })
    });
});