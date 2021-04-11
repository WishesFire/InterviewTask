function create_new_form() {
    const count_row = $('.form-control').val();
    if (count_row === 0 || !count_row) {
        alert("value 'row' will not be 0");
        return;
    }
    let path = String('/schema/') + slug
    let csrf_token = $('meta[name="csrf-token"]').attr('content')

    $.ajax({
        url: path,
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRF-TOKEN': csrf_token,
        },
        data: JSON.stringify({'status_client_task': 'sending', 'count': count_row}),
        success: function (response) {
            create_html();
            if (response['task_status'] === 'ready') {
                location.reload();
            }
            else {
                get_status(response['task_id'], path, csrf_token);
            }
        },
        error: function (exception) {
            console.log(exception)
            alert('Something wrong');
            location.reload();
        }
    });
}

function get_status(task_id, path, csrf_token) {
    $.ajax({
        url: path,
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRF-TOKEN': csrf_token,
        },
        data: JSON.stringify({'status_client_task': 'waiting', 'task_id': task_id}),
        success: function (response) {
            if (response['task_status'] === 'ready') {
                location.reload();
            }
            else {
                setTimeout(function (){
                    get_status(response['task_id'], path, csrf_token);
                }, 5000);
            }
        },
        error: function (exception) {
            alert('Something wrong');
            location.reload();
        }
    })
}

function create_html() {
    let block_temp = `
        <tr>
          <th scope="row">{number}</th>
          <td>{time}</td>
          <td>Processing</td>
          <td>
              <a href="#" download>Download</a>
          </td>
        </tr>`;
    let block_count = $('#main-download-block tr').length
    let full_date = get_date();
    let full_block = block_temp
        .replace('{number}', block_count)
        .replace('{time}', full_date)
    $('#main-download-block').append(full_block);
}

function get_date() {
    let today = new Date();
    let day = today.getDay();
    let month = today.getMonth() + 1;
    let year = today.getFullYear();
    return String(year + '-' + day + '-' + month)
}
