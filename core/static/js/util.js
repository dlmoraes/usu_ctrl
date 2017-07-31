var csrftoken = Cookies.get('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        iniciarCarregamento();
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    },
    complete: function () {
        fecharCarregamento();
    }
});

function iniciarCarregamento() {
    $(".loader-wrapper").attr('id', 'loader-wrapper');
    $(".loader").attr('id', 'loader');
    $("body").addClass("loader");
}

function fecharCarregamento() {
    $(".loader-wrapper").removeAttr('id');
    $(".loader").removeAttr('id');
    $("body").removeClass("loader");
}

function dataFormatada(data) {
    if (data == null) {
        return "";
    }
    var data = new Date(data);
    var dia = data.getDate();
    if (dia.toString().length == 1) {
        dia = "0" + dia;
    }
    var mes = data.getMonth() + 1;
    if (mes.toString().length == 1)
        mes = "0" + mes;
    var ano = data.getFullYear();
    return dia + "/" + mes + "/" + ano;
}

function msgNotificacao(tipo, titulo, msg) {
    swal({
        title: titulo,
        text: msg,
        html: true,
        confirmButtonColor: "#66BB6A",
        type: tipo,
        timer: 3500
    });
}

function codeHTML(code) {
    var html = "";
    switch (code) {
        case 'TLISTACAO':
            html = "<td class='text-center'>" +
                "<ul class='icons-list'>" +
                "<li class='dropdown'>" +
                "<a href='#' class='dropdown-toggle' data-toggle='dropdown'><i class='icon-menu9'></i></a>" +
                "<ul class='dropdown-menu dropdown-menu-right'>" +
                "<li><a href=':url1'><i class='icon-file-spreadsheet2'></i> Detalhes</a></li>" +
                "<li><a href=':url2'><i class='icon-attachment'></i> Anexar</a></li>" +
                "</ul>" +
                "</li>" +
                "</ul>" +
                "</td>";
            break;
        case 'TPLBTNS':
            html = '<button type="button" class="btn bg-teal-400 btn-labeled btn-rounded"><b><i class="icon-floppy-disk"></i></b></button>'
            break;
        default:
            html = "";
            break;
    }
    return html;
}

