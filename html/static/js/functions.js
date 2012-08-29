$(function(){

    // toggle dos blocks
    var block = $('.block');    
    block.find('h3').click(function(){
        $(this).next('.blockContent').slideToggle('fast');
    });
})