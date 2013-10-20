$(document).ready(function () {
    $('#slider').easySlider({
        auto: true,
        continuous: true,
        numeric: true,
        numericId: 'slider_contr',
        pause: 9000,
        prevId: 'slider1_prev',
        nextId: 'slider1_next'
    });
    $('#slider2').easySlider({
        auto: true,
        continuous: true,
        numeric: true,
        numericId: 'slider2_contr',
        pause: 12000,
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
        pause: 8000
    });

    member_block = $('#member_info');
    current_block_id = false;
    function client_open(block){
        var that = block;
        var url = $('.team_unit', that).attr('ajax_url');
        var block_id = $(block).attr('member_id');
        $('.ca-item.active').removeClass('active');

        if (current_block_id == block_id){
            current_block_id = false;
            member_block.slideUp('slow', function() {
                member_block.html('');
                scrollToElement($(that))
            });
        } else {
            current_block_id = block_id;
            $(block).addClass('active');
            member_block.slideUp(300, function() {
                member_block.html('');
                scrollToElement($(that));

                $.get(url, function(data) {
                    member_block.html(data);
                    member_block.slideDown(300, function(){
                        $("div.holder").jPages({
                            containerID: "ui_about",
                            perPage: 1,
                            next: '',
                            previous: '',
                            callback: function(pages, items){
                                if (pages.count < 2){
                                    $("div.holder").hide();
                                }
                            }
                        });

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
    }

    function client_block_open(){
        $('.clients_block').slideDown('normal', function() {
            scrollToElement(this);
            return false;
        });
    }
    function go_to_team(){
        scrollToElement($('#ca-container').parents('.wrapper'));
    }
    function go_to_about(){
        scrollToElement($('#about-subslider'));
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
        if (hash.substr(0,7) == 'member_'){
            var member_id = hash.substr(7);
            client_open($('.ca-item[member_id=' + member_id + ']')[0])
        }
    }
    $('.main_page #go_to_team').click(function(){go_to_team();return false;});
    $('.main_page #go_to_about').click(function(){go_to_about();return false;});
    $('.main_page #go_to_client').click(function(){client_block_open();return false;});
    $('.main_page .open_member').click(function(){client_open($('.ca-item[member_id=' + $(this).parents('.slide').attr('member_id') + ']')[0]);return false;});

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
    } else {
        /* ca-wrapper vertical align */
        var ca_wrapper_padding = parseInt(($('.ca-wrapper').width() - ($('.ca-wrapper .ca-item').width() * $('.ca-wrapper .ca-item').length))/2);
        $('.ca-wrapper').css('padding-left', ca_wrapper_padding);

    }

    $('.ca-item').click(function(){
        client_open(this);
        return false;
    });
    $('div').on('click', '.unit_info .close', function(){
        current_block_id = false;
            member_block.slideUp(300, function() {
                member_block.html('');
                $('.ca-item.active').removeClass('active');
                scrollToElement($('.ca-item'));
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
    $('.event_block .event_title').each(function(){
        var h = $(this).height();
        var sh = $('a', this).height();
        if (h > sh){
            var margin = parseInt((h - sh - 15)/2);
            $(this).css('padding-top', margin);
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

function scrollToElement( target ) {
    var topoffset = 30;
    var speed = 800;
    var destination = jQuery( target ).offset().top - topoffset;
    jQuery( 'html:not(:animated),body:not(:animated)' ).animate( { scrollTop: destination}, speed, function() {
        //window.location.hash = target;
    });
    return false;
}