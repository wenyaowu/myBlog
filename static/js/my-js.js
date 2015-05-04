/**
 * Created by evanwu on 5/4/15.
 */
$(function(){

    var $window = $(window);
    var $slideimage = $('#django-logo');
    var slidePoint = $slideimage.offset().bottom;

    $window.on('scroll', function(){

    if ( (slidePoint) < $window.scrollTop()) {
        $slideimage.animate({'right': '0px'}, 250);
    } else {
        $slideimage.stop(true).animate({'right': '-1400px'}, 250);
    }


    });
});