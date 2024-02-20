///////////
////JavaScript  for PostPage
/////////

$(function() {
    //Executed when js-menu-icon js is clicked

    $('.js-menu-icon').click(function() {
        ////$(this) :Self element, namely dic.js-menu-icon
        //nest() : Next to div.js-menu-icon, namely div.menu
        //toggle(): Switch show and hide
        $(this).next().toggle();
    })
})

