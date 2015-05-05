/**
 * Created by evanwu on 5/4/15.
 */
$(function(){

    var $window = $(window);
    var $slideimage = $('#djangoLogo');
    var slidePoint = $slideimage.offset().top;
     $('#test2').text("slidePoint:"+slidePoint);

    $(window).on('scroll', function(){
        $('#test').text("current point:"+$window.scrollTop())
        if ( slidePoint < $window.scrollTop()) {
            $slideimage.animate({'opacity': '1'}, 250);

        }else{ $slideimage.stop(true).animate({ 'opacity': '0.2' }, 250);}


    });
});
