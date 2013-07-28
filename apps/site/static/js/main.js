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
    $('#slider4').easySlider({
        auto: false,
        continuous: true,
        numeric: true,
        numericId: 'slider4_contr',
        pause: 7000
    });
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
    var mh = 0;
    $(".block").each(function () {
        var h_block = parseInt($(this).height());
        if (h_block > mh) {
            mh = h_block;
        }

    });
    $(".block").height(mh);
    $('.pw_info').click(function (e) {
        $('#info').addClass('show');
        return false;
    });
    $('#info').blur(function () {
        $('#info').addClass('hide');
        return false;
    });
});