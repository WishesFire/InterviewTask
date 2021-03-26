function createColumn() {
    let block = `
                <div class="block-column">
                    <div class="col-md-6">
                        <label for="inputCity" class="form-label">Column name</label>
                        <input type="text" class="form-control" id="inputCity">
                    </div>
                    <div class="col-md-4">
                        <label for="inputState" class="form-label">Type</label>
                        <select id="inputState" class="form-select">
                            <option selected>Choose...</option>
                            <option>...</option>
                        </select>
                    </div>
                    <div class="col-md-2">
                        <label for="inputZip" class="form-label">Order</label>
                        <input type="text" class="form-control" id="inputZip">
                    </div>
                    <div class="col-md-2">
                        <button type="button" class="btn btn-danger" onclick="deleteColumn()">Delete</button>
                    </div>
                </div>`
    $('.count-block').append(block);
    let change_count = $(".count-block").children().length;
    $('#secret_count').val(change_count)
}


function deleteColumn() {
    $(this).closest('.block-column').remove();
}