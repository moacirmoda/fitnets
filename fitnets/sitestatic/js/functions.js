$(function(){    

    window.setTimeout(function () {
        close_alert();
    }, 3000);

    var body = $('body');
    var block = $('.block');    

    // efeito em todos itens block para aparecem ao dar load
    body.hide();
    body.fadeIn(1000);

    // efeito de hide em tudo q tiver a classe
    $('.hide').hide();

    // toggle dos blocks
    block.find('h3').click(function(){
        $(this).next('.blockContent').slideToggle('fast');
    });

    // comentários do projeto
    $("#showComment").click(function(){
        $('.ultimas-publicacoes').fadeIn('slow');
    });

})

var box = $('.alert-box');
function close_alert() {
    $(".alert-box").animate({"top":'-100px'}, 600, 'easeOutQuart');
}