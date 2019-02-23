$(function ($) {
    "use strict"
    jQuery(window).on('load', function () {
        /*---------------------------------------------------
            Site Preloader
        ----------------------------------------------------*/
        var $sitePreloaderSelector = $('.site-preloader');
        $sitePreloaderSelector.fadeOut(500);
    });


    /* Offset start */
    var html_body = $('html, body'),
        nav = $('nav'),
        navOffset = nav.offset().top,
        $window = $(window);
    /* offset ends */

    $('#main-menu vnav a').on('click', function () {
        if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
            var target = $(this.hash);
            target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
            if (target.length) {
                html_body.animate({
                    scrollTop: target.offset().top - 30
                }, 1500);
                return false;
            }
        }
    });


    //review slider

    $('.feedback-slider').owlCarousel({
        loop: true,
        margin: 10,
        nav: true,
        responsive: {
            0: {
                items: 1
            },
            600: {
                items: 1
            },
            1000: {
                items: 1
            }
        }
    })

    // Team slider

    $('.slick_team').slick({
        dots: false,
        infinite: false,
        arrows: false,
        speed: 300,
        slidesToShow: 3,
        slidesToScroll: 1,
        responsive: [{
                breakpoint: 1024,
                settings: {
                    slidesToShow: 3,
                    slidesToScroll: 1,
                    infinite: true,
                    dots: true
                }
            },
            {
                breakpoint: 992,
                settings: {
                    slidesToShow: 2,
                    slidesToScroll: 1
                }
            },
            {
                breakpoint: 768,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1
                }
            }
        ]
    });





    // veno box light box plugin
    $('.venobox').venobox();

    /*---------------------------------------------------
            Click To Top
        ----------------------------------------------------*/
    $(document).on('click', '.totop a[href=#top]', function () {

        $('body,html').animate({

            scrollTop: 0

        }, 600);

        return false;

    });

    jQuery(window).on('scroll', function () {

        /*---------------------------------------------------
            Click To Top
        ----------------------------------------------------*/
        var $scrollTopSelector = $('.totop');
        if ($(this).scrollTop() > 550) {
            $scrollTopSelector.fadeIn();
        } else {
            $scrollTopSelector.fadeOut();
        }

    })

    // wow js 
    new WOW().init();



});



// Project             : Raxio - Micro Freelancing Marketplace.
// Version             : 1.0
// Author              : Thesoftking
// Front-end developer : Mamunur Rashid