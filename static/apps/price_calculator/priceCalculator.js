// $("#footer").html('© ' + new Date().getFullYear() + ' Fii HOU SWD');
var tkn = jQuery("[name=csrfmiddlewaretoken]").val();
console.log(tkn);

var stock = {
    updateButton : function () {
        // get the values of input fields
        var stockInput = $('input#input_stock_symbol').val();
        var startDate  = $('input#input_start_date').val();
        var endDate    = $('input#input_end_date').val();

        $('#spinner').show();

        $.ajax({
            // send request to views
            type: 'POST',
            // look for the right function in views.py based on the path in urls.py
            url: 'stock-price',
            // send over data collected from front end to views.py
            data: {
                'function'     : 'submit()',
                'stock_symbol' : stockInput,
                'start_date'   : startDate,
                'end_date'     : endDate,
                'csrfmiddlewaretoken': tkn
            },
            dataType: 'json',
            success: function (response) {
                $('#spinner').hide();

                // get the data from runfunction(db_conn,'main_stock_get_price_fn', sp_params)
                let object = response.stock_prices;

                $('#stock-price-table').DataTable();
                $("#stock-price-table-tbody").children().remove();
                // Reset datatable every time new input entered
                $("#stock-price-table").DataTable().clear();

                // If table is initialized
                if ($.fn.DataTable.isDataTable('#stock-price-table')){
                    // Destroy existing table
                    $('#stock-price-table').DataTable().destroy();
                }                    

                let stock_price_table_body = $('#stock-price-table tbody');
                let price_template;

                for (let i = 0; i < object.length; i++) {
                    price_template += "<tr>";
                    price_template += "<td>" + object[i][0]  + "</td>";    // company
                    price_template += "<td>" + object[i][6]  + "</td>";    // date
                    price_template += "<td>" + object[i][1]  + "</td>";    // open
                    price_template += "<td>" + object[i][2]  + "</td>";    // high
                    price_template += "<td>" + object[i][3]  + "</td>";    // low
                    price_template += "<td>" + object[i][4]  + "</td>";    // close
                    price_template += "<td>" + object[i][5]  + "</td>";    // volume
                    price_template += "</tr>";  
                }
                stock_price_table_body.append(price_template);

                // Show 5 entries instead of 10 as default
                $('#stock-price-table').DataTable({pageLength: 10});

                // $('input#input_stock_symbol').val('');

            },
            error: function (response) {
                console.log(response);
            },
            complete: function () {
                console.log("COMPLETED");
                $('#spinner').hide();
            }
        })
    }
}