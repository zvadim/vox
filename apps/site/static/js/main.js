$(document).ready(function () {
    $('#slider').easySlider({
        auto: true,
        continuous: true,
        numeric: true,
        numericId: 'slider_contr',
        pause: 7000,
        prevId: 'slider1_prev',
        nextId: 'slider1_next'
    });
    $('#slider2').easySlider({
        auto: true,
        continuous: true,
        numeric: true,
        numericId: 'slider2_contr',
        pause: 10000,
        fadeEffect: true
    });
    $('#slider3').easySlider({
        auto: true,
        continuous: true,
        numeric: true,
        numericId: 'slider3_contr',
        pause: 18000,
        fadeEffect: true
    });
    $('.gallery_slider').easySlider({
        auto: true,
        continuous: true,
        numeric: true,
        numericId: 'gallery_slider_contr',
        pause: 5000
    });


    function client_block_open(){
        $('.clients_block').slideDown('normal', function() {
            $(document.body).animate({
                "scrollTop": $(this).offset().top
            }, 700, "swing");
            return false;
        });
    }
    function go_to_team(){
        $(document.body).animate({
            "scrollTop": $('#ca-container').parents('.wrapper').offset().top - 10
        }, 700, "swing");
    }
    function go_to_about(){
        $(document.body).animate({
            "scrollTop": $('#about-subslider').offset().top - 10
        }, 700, "swing");
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
        if (hash == 'about'){
            go_to_about();
        }
    }
    $('.main_page #go_to_team').click(function(){go_to_team();return false;});
    $('.main_page #go_to_about').click(function(){go_to_about();return false;});
    $('.main_page #go_to_client').click(function(){client_block_open();return false;});


    /* Показывает/прячем блок клиентов */
    $('.otzivi_slider .arrow').click(function(){
        client_block_open();
        return false;
    });
    $('.kli_tit .close').click(function(){
        $('.clients_block').slideUp();
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
    member_block = $('#member_info');
    current_block_id = false;
    $('.ca-item').click(function(){
        that = this;
        url = $('.team_unit', that).attr('ajax_url');
        block_id = $(this).attr('member_id');
        $('.ca-item.active').removeClass('active');

        if (current_block_id == block_id){
            current_block_id = false;
            member_block.slideUp('slow', function() {
                member_block.html('');
                $(document.body).animate({
                    "scrollTop": $(that).offset().top
                }, 800, "swing");
            });
        } else {
            current_block_id = block_id;
            $(this).addClass('active');
            member_block.slideUp('slow', function() {
                member_block.html('');
                $(document.body).animate({
                    "scrollTop": $(that).offset().top
                }, 800, "swing");


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
        }
    });
    $('div').on('click', '.unit_info .close', function(){
        current_block_id = false;
            member_block.slideUp('slow', function() {
                member_block.html('');
                $('.ca-item.active').removeClass('active');
                $(document.body).animate({
                    "scrollTop": $('.ca-item').offset().top
                }, 200, "swing");
            });
    });

    $('.button_print').click(function(){
        window.print();
        return false;
    });

    $('.button_share').click(function(){
        shareOnFacebook();
        return false;
    });

    $('#bottom_logo').click(function(){
        $(document.body).animate({
            "scrollTop": 0
        }, 300, "swing");
    });


    /* event block vertical align */
    $('.event_block').each(function(){
        var h = $(this).height();
        var sh = $('.event_title', this).height();
        if (h > sh){
            var margin = parseInt((h - sh - 15)/2);
            $('.event_title', this).css('padding-top', margin);
        }
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