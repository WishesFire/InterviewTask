function deleteSchema(el) {
    $.ajax({
        url: '/profile',
        headers: {'X-CSRF-TOKEN': $('meta[name="csrf-token"]').attr('content'), 'Content-Type': 'application/json'},
        method: 'POST',
        data: JSON.stringify({'status': 'delete', 'name': $(el).closest('.block-row').find('.schemas-name').text()}),
        success: function (response) {
            $(el).closest('.block-row').remove();
        },
        error: function (exception) {
            alert('Something wrong');
            location.reload();
        }
    })}