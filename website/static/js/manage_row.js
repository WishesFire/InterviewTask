function createColumn() {
    let block = `
                <div class="block-column">
                    <div class="col-md-6">
                        <label for="inputCity" class="form-label">Column name</label>
                        <input minlength="4" name="column_name" type="text" class="form-control" id="inputCity">
                    </div>
                    
                    <div class="col-md-4">
                        <label for="inputState" class="form-label">Type</label>
                        <select name="column_type" id="inputState" class="form-select">
                            <option selected>NAME</option>
                            <option>JOB</option>
                            <option>EMAIL</option>
                            <option>DOMAIN</option>
                            <option>PHONE</option>
                            <option>COMPANY</option>
                            <option>INT</option>
                            <option>ADDRESS</option>
                            <option>DATE</option>
                        </select>
                    </div>
                    
                    <div class="col-md-2">
                        <label for="inputZip" class="form-label">Order</label>
                        <input name="column_order" type="number" class="form-control" id="inputZip">
                    </div>
                    
                    <div class="col-md-2">
                        <button type="button" class="btn btn-danger" onclick="deleteColumn(this)">Delete</button>
                    </div>
                </div>`

    $('.count-block').append(block);
    let change_count = $(".count-block").children().length;
    $('#secret_count').val(change_count)
}


function deleteColumn(el) {
    $(el).closest('.block-column').remove();

}