$(function(){
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function(pos){

            let long = pos.coords.longitude
            let lat = pos.coords.latitude

            $.ajax({
                    url: 'https://dapi.kakao.com/v2/local/geo/coord2address.json?x=' + long + '&y=' + lat,
                    type: 'GET',
                    headers: {
                        'Authorization': 'KakaoAK ac6a4068ede062398404530f4a813347'
                    },
                    success: function (data) {
                    let road_city = data['documents']['0']['road_address']['region_1depth_name'];
                    let road_region = data['documents']['0']['road_address']['region_2depth_name'];

                        console.log(road_city, road_region);
                        $('#current_location').text(road_city +' '+ road_region)
                    },
                    error: function(e) {
                    console.log(e);
                    }
                });
            })
        }
    else{
        alert("error")
    }

})

function search_result() {
    let result = $('#search').val()
    alert(result)
    location.href="https://map.naver.com/v5/search/" + result

    result.empty()
}

function open_box() {
    $('#mypost').show()
}

function close_box() {
    $('#mypost').hide()
}