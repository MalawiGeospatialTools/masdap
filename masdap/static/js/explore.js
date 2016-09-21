$(function() {

    $(".datepicker").datetimepicker({autoclose:true});
  
    $("#slide-pane a.toggle-pane").click(function(e) {
        e.preventDefault();
        var span$ = $("#slide-pane").parents(".col-md-3");
        if(!span$.is('.hidden')) {
            span$.addClass("hidden").animate({
                marginLeft: "-310px"
            }, 500, function() {
                setContentWidth();
            });
            $(this).find("i").attr("class", "fa fa-angle-right fa-lg");
        } else {
            span$.removeClass("hidden").animate({
                marginLeft: "0px"
            }, 500, function() {
                setContentWidth();
            });
            $(this).find("i").attr("class", "fa fa-angle-left fa-lg");
        }
    });
    $("nav a.toggle-nav").click(function(e) {
        e.preventDefault();
        if ($(this).parents("h4").siblings(".nav").is(":visible")) {
            $(this).parents("h4").siblings(".nav").slideUp();
            $(this).find("i").attr("class", "fa fa-angle-right fa-lg");
        } else {
            $(this).parents("h4").siblings(".nav").slideDown();
            $(this).find("i").attr("class", "fa fa-angle-down fa-lg");
        }
    });
});

function setContentWidth() {
    var lm = parseInt($("#slide-pane").parents(".col-md-3").css("marginLeft").replace("px", "")) + 51;
    var w = $("#contain-slider").width() - ($("#slide-pane").outerWidth() + lm);
    $(".tab-content").css('width', w + "px");
}