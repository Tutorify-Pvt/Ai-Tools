$(document).ready(function () {
    var slideAmount = 75;

    $('.next-slide').click(function () {
        $('.slider-container').animate({scrollLeft: '+=' + slideAmount}, 'slow');
    });

    $('.prev-slide').click(function () {
        $('.slider-container').animate({scrollLeft: '-=' + slideAmount}, 'slow');
    });

    $('.slider-button').click(function () {
        var $this = $(this);
        if ($this.hasClass('prev-slide')) {
            $('.slider-container').animate({scrollLeft: '-=' + slideAmount}, 'slow');
        } else if ($this.hasClass('next-slide')) {
            $('.slider-container').animate({scrollLeft: '+=' + slideAmount}, 'slow');
        }
    });
});