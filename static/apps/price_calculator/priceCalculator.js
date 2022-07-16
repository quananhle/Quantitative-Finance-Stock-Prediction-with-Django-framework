// $("#footer").html('© ' + new Date().getFullYear() + ' Fii HOU SWD');
var tkn = jQuery("[name=csrfmiddlewaretoken]").val();
console.log(tkn);

var stock = {
    updateButton : function () {
        // // If table is initialized
        // if ($.fn.DataTable.isDataTable('#stock-price-table')){
        //     // Destroy existing table
        //     $('#stock-price-table').DataTable().destroy();
        // }
        // // check if price table is a Data Table
        // if ($.fn.DataTable.isDataTable('#stock-price-table') ) {
        //     $('#stock-price-table').DataTable().clear();
        //     $('#stock-price-table').DataTable().destroy();
        //     $('#stock-price-table').children().remove();
        //     $('#stock-price-table tbody').children().remove();
        // }

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

                console.log(object);

                if (response.stock_prices.length > 1) {
                    $('#stock-price-table').DataTable();

                    $("#stock-price-table tbody").children().remove();
                    $("#stock-price-table-tbody").children().remove();
                    // Reset datatable every time new input entered
                    $("#stock-price-table").DataTable().clear();

                    let stock_price_table_body    = $('#stock-price-table tbody');
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
                    $('#stock-price-table').DataTable({pageLength: 5});
                }
                else {
                    $('#price-company').html(object[0][0]);
                    $('#price-open'   ).html(object[0][1]);
                    $('#price-high'   ).html(object[0][2]);
                    $('#price-low'    ).html(object[0][3]);
                    $('#price-close'  ).html(object[0][4]);
                    $('#price-volume' ).html(object[0][5]);
                    $('#price-date'   ).html(object[0][6]);
                }





                // $('#inputKeypart')             .attr("placeholder", object[0][1]).val('');
                // $('#inputMaskRule')            .val('');               
                // $('#inputCategoryID')          .val('');
                // $('#inputSpanishDescription')  .val('');    
                // $('#inputFraccNico')           .val('');    
                // $('#inputUOMValue')            .val('');    
                // $('#inputHstCode')             .val('');    
                // $('#inputFraccDigits')         .val('');
                // $('#inputTechnicalDescription').val('');

                // // display success message
                // $('#spinner').hide();
                // $("#successMsgModal").append(successMessageModal);
                // $('#successMsg').append("Updated Successfully");

            },
            error: function (response) {
                console.log(response);
                // $("#successMsgModal").children().remove();
                // var error = response["responseJSON"]["result"];
                // console.log(error);
                // errorMessageBlock.append(errorMessageModal);
                // $('#errorMsg').append(error);
                // // clear input fields at failed.
                // $('#inputKeypart')             .val('');
                // $('#inputMaskRule')            .val('');
                // $('#inputCategoryID')          .val('');
                // $("#noInputPlantCode")         .val('');
                // $("#noInputSAPChangedDate")    .val('');
                // $('#inputSpanishDescription')  .val('');
                // $('#inputFraccNico')           .val('');
                // $('#inputUOMValue')            .val('');
                // $('#inputHstCode')             .val('');
                // $('#inputFraccDigits')         .val('');
                // $('#inputTechnicalDescription').val('');
            },
            complete: function (response) {
                console.log("COMPLETED");
                $('#spinner').hide();
            }
        })
    }
}