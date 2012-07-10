/**
 * Created with PyCharm.
 * User: ts.trinity
 * Date: 05.07.12
 * Time: 12:32
 * To change this template use File | Settings | File Templates.
 */


$().ready(function () {
    var map = new AddPointMap();
    map.init();
});


function AddPointMap() {
    var current_marker;
    _this = this;
    this.prototype = new Map();
    this.prototype.init();

    google.maps.event.addListener(_this.prototype.map, 'click', function (event) {
        _this.addMarker(event.latLng);
    });
    this.init = function() {

        $("#save_button").click(function () {
            if ($("#add_post_form").valid()){
                $("#add_post_form").submit();
                _this.saveToDB();
            }
        });

        var providers_comboBox = $("#provider");

        $.ajax({
            type: "POST",
            url: "/providers/getAllProviders",
            success: function(data){
                $.each(data, function (i, item) {
                    providers_comboBox.append('<option value="' + item.pk + '">' + item.fields.name + '</option>');
                });
            },
            error: function(){
                alert('Error while trying to get providers list');
            }
        })


    }

    this.saveToDB = function() {
        //LatLng object for gathering coordinates;
        var position = _this.current_marker.getPosition();

        var ajaxData = {
            name: $("#name").val(),
            provider: $("#provider option:selected").val(),
            signal_quality: $('input[name=signal_quality]:radio:checked').val(),
            coordinate_latitude: position.lat(),
            coordinate_longitude: position.lng()
        }

        data = { "firstName": "Brett" };

        $.ajax({
                type : "POST",
                url : "/points/savePointToDB",
                contentType: "application/json",
                data : ajaxData,
                success: function (data) {
                    if (data.status == "ok") {
                        location.replace('/points/');
                    }
                },
                error: function() {
                    alert("Ошибка добавления в БД");
                }
        });
    }

    this.addMarker = function(location) {
        if (this.current_marker) {
            this.current_marker.setMap(null);
        }
        this.current_marker = new google.maps.Marker({
            position: location,
            map: _this.prototype.map,
            zIndex: 999
        });
    }


}


