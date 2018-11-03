$(document).ready(function(){
    // Initialize mobile menu
    $('.sidenav').sidenav();

    // Initialize materialize data picker
    $('.datepicker').datepicker({'format': 'yyyy-mm-dd'});
    $('select').formSelect();
});