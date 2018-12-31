$(document).ready(function () {
    $("#ok").click(function () {

        if ($("#ac").text() == '0') {
            $.ajax({

                url: 'https://api.parkline.cc/api/token',
                type: 'post',
                dataType: 'json',
                data: {"apiid": "bl397233b7de02c055", "apikey": "da5cbd210dbd9e994a9fdf5731aaae51"},

                success: function (data) {


                    $.ajax({

                        url: '/gettoken/',
                        type: 'post',
                        dataType: 'json',
                        data: {"expires_in": data.expires_in, "access_token": data.access_token, "ntype": "new"},

                        success: function (data1) {

                            alert('new OK!');


                        }

                    })


                }

            })
        }
        else {
            $.ajax({

                url: '/gettoken/',
                type: 'post',
                dataType: 'json',
                data: {"expires_in": $("#ex").text(), "access_token": $("#ac").text(), "ntype": "old"},

                success: function (data1) {

                    alert('old OK!');


                }

            })
        }


    })


})