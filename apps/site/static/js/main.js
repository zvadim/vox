$(document).ready(function () {
    $('#slider').easySlider({
        auto: true,
        continuous: true,
        numeric: true,
        numericId: 'slider_contr',
        pause: 5000
    });
    $('#slider2').easySlider({
        auto: true,
        continuous: true,
        numeric: true,
        numericId: 'slider2_contr',
        pause: 8000
    });
    $('#slider3').easySlider({
        auto: true,
        continuous: true,
        numeric: true,
        numericId: 'slider3_contr',
        pause: 9500
    });



    function client_block_open(){
        $('.clients_block').slideDown('slow', function() {
            $(document.body).animate({
                "scrollTop": $(this).offset().top
            }, 2000, "swing");
            return false;
        });
    }
    function go_to_team(){
        $(document.body).animate({
            "scrollTop": $('#ca-container').parents('.wrapper').offset().top - 10
        }, 2000, "swing");
    }
    /* скользим к блоку клиентов/команды */
    if (location.hash.length > 1) {
        var hash = location.hash.replace(/^#/, '');
        if (hash == 'clients'){
            client_block_open();
        }
        if (hash == 'team'){
            go_to_team();
        }
    }
    $('.main_page #go_to_team').click(function(){go_to_team();return false;});
    $('.main_page #go_to_client').click(function(){client_block_open();return false;});


    /* Показывает/прячем блок клиентов */
    $('.otzivi_slider .arrow').click(function(){
        client_block_open();
        return false;
    });
    $('.kli_tit .close').click(function(){
        $('.clients_block').slideUp('slow');
        return false;
    });

    /* Блок с клиентами на главной. Добавляем пустые блоки */
    cl_num_max = 24;
    cl_num = $('div', '.klienti').length;
    for (b=cl_num;b<cl_num_max;b=b+1){
        div = $('<div/>');
        if (b>=8 && b<16) div.addClass('odd');
        $('.klienti').append(div);
    }



    /* Карусель и блок мембера */
    if ($('.ca-item').length > 5){
        $('#ca-container').contentcarousel({
            // Скорость анимации проскальзывания
            sliderSpeed: 500,
            // Эффект анимации проскальзывания
            sliderEasing: 'easeOutExpo',
            // Скорость анимации открытия/закрытия пункта
            itemSpeed: 500,
            // Скорость анимации открытия/закрытия пункта
            itemEasing: 'easeOutExpo',
            // Количество пунктов для прокручивания за один шаг
            scroll: 1
        });
    }
    member_block = $('#member_info')
    $('.ca-item').click(function(){
        that = this;
        member_block.slideUp('slow', function() {
            member_block.html('');
            $(document.body).animate({
                "scrollTop": $(that).offset().top
            }, 2000, "swing");

            url = $('.team_unit', that).attr('ajax_url');
            $.get(url, function(data) {
                member_block.html(data);
                member_block.slideDown('slow', function(){
                    $('.member_block_slider').easySlider({
                        auto: false,
                        continuous: true,
                        numeric: true,
                        numericId: 'member_block_slider_contr',
                        pause: 7000
                    });
                });
            })
        });
    });


});

$(window).load(function(){

    var mh = 0;
    $(".block").each(function () {
        var h_block = parseInt($(this).height());
        if (h_block > mh) {
            mh = h_block;
        }

    });
    $(".block").height(mh);
});