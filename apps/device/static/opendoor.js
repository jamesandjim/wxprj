$(document).ready(function () {
    $("#open").click(function () {
        var acv = $("#ac").text();
        alert(acv);

        $.ajax({

            url: 'https://api.parkline.cc/api/devicecgi',
            type: 'post',
            dataType: 'json',
            data: {"token": acv, "typeid": "01", "devid": "212139", "lockid": "01"},

            success: function (data) {
                alert("开门成功！")
            }


        })

    })
})


