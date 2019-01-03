$(document).ready(function () {
    $("#status").click(function () {
        var acv = $("#ac").text();

        $.ajax({

            url: 'https://api.parkline.cc/api/statuscgi',
            type: 'post',
            dataType: 'json',
            data: {"token": acv, "devid": "212139", "lockid": "01"},

            success: function (data) {
                alert(JSON.stringify(data))
            }


        })

    })
})


