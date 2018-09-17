$(document).ready(function(){
    $('.menu ul li.drop-down > a').on('click',function(e){
        e.preventDefault();
        $(this.nextElementSibling).slideToggle(300);
    });
});
