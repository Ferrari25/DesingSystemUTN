
var checkbox = document.querySelector('input[name="fav_language"]');
var button = document.querySelector('.button-pay');

checkbox.addEventListener('change', function() {
    if(this.checked) {
        button.style.backgroundColor = '#000000'; 
    } else {
        
        button.style.backgroundColor = ''; 
    }
});
