/*window.onload(navigator.geolocation.getCurrentPosition((position) => {
    doSomething(position.coords.latitude, position.coords.longitude);
})
)
function location(){
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition()
    }

    $('#location').text()
}*/

function search_result() {
    let result = $('#search').val()
    alert(result)
    location.href="https://map.naver.com/v5/search/" + result

    result.empty()
}
