$(function(){

    var body = $('body');
    var block = $('.block');    

    // efeito em todos itens block para aparecem ao dar load
    body.hide();
    body.fadeIn(1000);

    // toggle dos blocks
    block.find('h3').click(function(){
        $(this).next('.blockContent').slideToggle('fast');
    });
})