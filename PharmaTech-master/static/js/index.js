//======================== index slider ==========================================
let slideIndex = 0;
showSlides();

function showSlides() {
  let i;
  let slides = document.getElementsByClassName("mySlides");
  let dots = document.getElementsByClassName("dot");
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";  
  }
  slideIndex++;
  if (slideIndex > slides.length) {slideIndex = 1}    
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";  
  dots[slideIndex-1].className += " active";
  setTimeout(showSlides, 2000); // Change image every 2 seconds
}
//=================================== reveal content ==================================================
$(document).ready(function() {
  $('.box-carousel').slick({
 dots: false,
 arrows: true,
 slidesToShow: 5,
 slidesToScroll: 1,
 prevArrow: "<button type='button' class='mission-prev-arrow'></button>",
 nextArrow: "<button type='button' class='mission-next-arrow'></button>"
});

});
function reveal() {
  var reveals = document.querySelectorAll(".reveal");

  for (var i = 0; i < reveals.length; i++) {
    var windowHeight = window.innerHeight;
    var elementTop = reveals[i].getBoundingClientRect().top;
    var elementVisible = 150;

    if (elementTop < windowHeight - elementVisible) {
      reveals[i].classList.add("active");
    } else {
      reveals[i].classList.remove("active");
    }
  }
}

window.addEventListener("scroll", reveal);




//======================================= labtest container index ============================
const prev = document.querySelector(".prev");
const next = document.querySelector(".next");
const carousel = document.querySelector(".carousel-container");
const track = document.querySelector(".track");
let width = carousel.offsetWidth;
let index = 0;
window.addEventListener("resize", function () {
  width = carousel.offsetWidth;
});
next.addEventListener("click", function (e) {
  e.preventDefault();
  index = index + 1;
  prev.classList.add("show");
  track.style.transform = "translateX(" + index * -width + "px)";
  if (track.offsetWidth - index * width < index * width) {
    next.classList.add("hide");
  }
});
prev.addEventListener("click", function () {
  index = index - 1;
  next.classList.remove("hide");
  if (index === 0) {
    prev.classList.remove("show");
  }
  track.style.transform = "translateX(" + index * -width + "px)";
});
(function () {
  "use strict";

  var carousels = function () {
    $(".owl-carousel1").owlCarousel({
      loop: true,
      center: true,
      margin: 0,
      responsiveClass: true,
      nav: false,
      responsive: {
        0: {
          items: 1,
          nav: false
        },
        680: {
          items: 2,
          nav: false,
          loop: false
        },
        1000: {
          items: 3,
          nav: true
        }
      }
    });
  };

  (function ($) {
    carousels();
  })(jQuery);
})();












// for animation 

$(document).ready(function(){
  $('.pp-quote').click(function(){
    $('.pp-quote').removeClass("active");
    $(this).addClass("active");
});
});

$(document).ready(function(){
    
       // hide-top

        $('.li-quote-1').click(function(e){ 
            e.stopPropagation();
            $(".show").addClass('hide-top');
            $(".hide-top").removeClass('show');
            $('.quote-text-1').addClass('show');
            $('.quote-text-1').removeClass('hide-bottom');             
        });

        $('.li-quote-2').click(function(e){ 
            e.stopPropagation();
            $(".show").addClass('hide-top');
            $(".hide-top").removeClass('show');
            $('.quote-text-2').addClass('show');             
            $('.quote-text-2').removeClass('hide-bottom');
        });

        $('.li-quote-3').click(function(e){ 
            e.stopPropagation();
            $(".show").addClass('hide-top');
            $(".hide-top").removeClass('show');         
            $('.quote-text-3').addClass('show');             
            $('.quote-text-3').removeClass('hide-bottom');
        });
        $('.li-quote-4').click(function(e){ 
            e.stopPropagation();
            $(".show").addClass('hide-top');
            $(".hide-top").removeClass('show');      
            $('.quote-text-4').addClass('show');             
            $('.quote-text-4').removeClass('hide-bottom');
        });
        $('.li-quote-5').click(function(e){ 
            e.stopPropagation();
            $(".show").addClass('hide-top');
            $(".hide-top").removeClass('show');      
            $('.quote-text-5').addClass('show');             
            $('.quote-text-5').removeClass('hide-bottom');
        });
        $('.li-quote-6').click(function(e){ 
            e.stopPropagation();
            $(".show").addClass('hide-top');
            $(".hide-top").removeClass('show');      
            $('.quote-text-6').addClass('show');             
            $('.quote-text-6').removeClass('hide-bottom');
        });
        $('.li-quote-7').click(function(e){ 
            e.stopPropagation();
            $(".show").addClass('hide-top');
            $(".hide-top").removeClass('show');      
            $('.quote-text-7').addClass('show');             
            $('.quote-text-7').removeClass('hide-bottom');
        });
        $('.li-quote-8').click(function(e){ 
            e.stopPropagation();
            $(".show").addClass('hide-top');
            $(".hide-top").removeClass('show');      
            $('.quote-text-8').addClass('show');             
            $('.quote-text-8').removeClass('hide-bottom');
        });
           
    
});

$(document).ready(function () {
    var itemsMainDiv = ('.MultiCarousel');
    var itemsDiv = ('.MultiCarousel-inner');
    var itemWidth = "";

    $('.leftLst, .rightLst').click(function () {
        var condition = $(this).hasClass("leftLst");
        if (condition)
            click(0, this);
        else
            click(1, this)
    });

    ResCarouselSize();




    $(window).resize(function () {
        ResCarouselSize();
    });

    //this function define the size of the items
    function ResCarouselSize() {
        var incno = 0;
        var dataItems = ("data-items");
        var itemClass = ('.item');
        var id = 0;
        var btnParentSb = '';
        var itemsSplit = '';
        var sampwidth = $(itemsMainDiv).width();
        var bodyWidth = $('body').width();
        $(itemsDiv).each(function () {
            id = id + 1;
            var itemNumbers = $(this).find(itemClass).length;
            btnParentSb = $(this).parent().attr(dataItems);
            itemsSplit = btnParentSb.split(',');
            $(this).parent().attr("id", "MultiCarousel" + id);


            if (bodyWidth >= 1200) {
                incno = itemsSplit[3];
                itemWidth = sampwidth / incno;
            }
            else if (bodyWidth >= 992) {
                incno = itemsSplit[2];
                itemWidth = sampwidth / incno;
            }
            else if (bodyWidth >= 768) {
                incno = itemsSplit[1];
                itemWidth = sampwidth / incno;
            }
            else {
                incno = itemsSplit[0];
                itemWidth = sampwidth / incno;
            }
            $(this).css({ 'transform': 'translateX(0px)', 'width': itemWidth * itemNumbers });
            $(this).find(itemClass).each(function () {
                $(this).outerWidth(itemWidth);
            });

            $(".leftLst").addClass("over");
            $(".rightLst").removeClass("over");

        });
    }


    //this function used to move the items
    function ResCarousel(e, el, s) {
        var leftBtn = ('.leftLst');
        var rightBtn = ('.rightLst');
        var translateXval = '';
        var divStyle = $(el + ' ' + itemsDiv).css('transform');
        var values = divStyle.match(/-?[\d\.]+/g);
        var xds = Math.abs(values[4]);
        if (e == 0) {
            translateXval = parseInt(xds) - parseInt(itemWidth * s);
            $(el + ' ' + rightBtn).removeClass("over");

            if (translateXval <= itemWidth / 2) {
                translateXval = 0;
                $(el + ' ' + leftBtn).addClass("over");
            }
        }
        else if (e == 1) {
            var itemsCondition = $(el).find(itemsDiv).width() - $(el).width();
            translateXval = parseInt(xds) + parseInt(itemWidth * s);
            $(el + ' ' + leftBtn).removeClass("over");

            if (translateXval >= itemsCondition - itemWidth / 2) {
                translateXval = itemsCondition;
                $(el + ' ' + rightBtn).addClass("over");
            }
        }
        $(el + ' ' + itemsDiv).css('transform', 'translateX(' + -translateXval + 'px)');
    }

    //It is used to get some elements from btn
    function click(ell, ee) {
        var Parent = "#" + $(ee).parent().attr("id");
        var slide = $(Parent).attr("data-slide");
        ResCarousel(ell, Parent, slide);
    }

});