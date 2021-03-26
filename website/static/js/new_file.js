function create_new_form() {
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
    $('#main-download-block tbody').append(full_block);


}

function get_date() {
    let today = new Date();
    let day = today.getDay();
    let month = today.getMonth() + 1;
    let year = today.getFullYear();
    return String(year + '-' + day + '-' + month)
}