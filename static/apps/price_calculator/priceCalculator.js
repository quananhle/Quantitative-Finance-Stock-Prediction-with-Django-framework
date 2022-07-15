// $("#footer").html('© ' + new Date().getFullYear() + ' Fii HOU SWD');
var tkn = jQuery("[name=csrfmiddlewaretoken]").val();
console.log(tkn);

var stock = {
    updateButton : function () {
        $('#stock-price-table').children().remove();

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

                if (response.stock_prices.length > 1) {
                    $('#stock-price-table').DataTable();
                }

                // // reset values in both table
                // form_model_manager_master_table.children().remove();
                // form_model_manager_data_table.children().remove();
                
                // // get the data from runfunction(db_conn,'mfg_model_manager_update_fn', sp_params)
                // let object = response.mm_info;

                // let master_template; let data_template;

                // for (let i = 0; i < object.length; i++) {
                //     master_template += "<tr>"; data_template += "<tr>";
                //     master_template += "<td>" + object[i][0]  + "</td>";    // model id
                //     master_template += "<td>" + object[i][1]  + "</td>";    // keypart
                //     master_template += "<td>" + object[i][2]  + "</td>";    // mask rule
                //     master_template += "<td>" + object[i][3]  + "</td>";    // category id
                //     master_template += "<td>" + object[i][4]  + "</td>";    // plant code
                //     master_template += "<td>" + object[i][5]  + "</td>";    // sap changed date
                //     data_template   += "<td>" + object[i][6]  + "</td>";    // spanish description
                //     data_template   += "<td>" + object[i][7]  + "</td>";    // fracc nico
                //     data_template   += "<td>" + object[i][8]  + "</td>";    // uom value
                //     data_template   += "<td>" + object[i][9]  + "</td>";    // hst code
                //     data_template   += "<td>" + object[i][10] + "</td>";    // fracc digit
                //     data_template   += "<td>" + object[i][11] + "</td>";    // technnical description
                //     master_template += "</tr>"; data_template += "</tr>";   
                // }
                // form_model_manager_master_table.append(master_template);
                // form_model_manager_data_table.append(data_template);

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