// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    // 모든 Ajax 요청 전에 호출되는 함수를 지정
    beforeSend: function(xhr, settings) {
        // CSRF Token 설정이 필요한 요청이면
        if ( !csrfSafeMethod(settings.type) && !this.crossDomain ) {
            // Token 값을 가져와서, 요청 헤더에 심어줍니다.
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});