var errorMessageModal = '<div class="row justify-content-md-center"><div class="col-md-auto"><div class="alert alert-danger" role="alert">';
errorMessageModal += '<h6 class="alert-heading" style="font-weight: bold;">Error!</h6><p class="mb-0" id="errorMsg"></p></div></div></div>';

var main = {
    show_error_message: function (message) {
        let messageBlock = $("#errorMsgModal");
        messageBlock.children().remove();
        messageBlock.append(errorMessageModal);
        $('#errorMsg').text(message);
    },
    clean_error_message: function () {
        let messageBlock = $("#errorMsgModal");
        messageBlock.children().remove();
    },
}

