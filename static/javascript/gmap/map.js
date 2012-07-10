/*
 * Created with PyCharm.
 * User: ts.trinity
 * Date: 27.06.12
 * Time: 11:30
 * To change this template use File | Settings | File Templates.
 */


function Map()
{
    var _this = this;
    this.map = null;
    this.geocoder = null;
    this.markerClusterer = null;

    this.center_longitude = 53.90221226318637;
    this.center_latitude = 27.56163356802483;

    this.providers = null;

    this.init = function(){
        _this.geocoder = new google.maps.Geocoder();
        if (_this.map == null) {
            var center = new google.maps.LatLng(_this.center_longitude, _this.center_latitude);
            var options = {
                zoom: 11,
                center: center,
                mapTypeId: google.maps.MapTypeId.ROADMAP
            };
            _this.map = new google.maps.Map(document.getElementById("map"), options);
        }

        _this.getProviders();
        _this.getPoints("");
    }

    this.codeAddress = function(){
        var address = $("#search_form_points").val();
        _this.geocoder.geocode( {'address' : address},function(results, status) {
            if (status == google.maps.GeocoderStatus.OK) {
                _this.map.setCenter(results[0].geometry.location);
                _this.map.setZoom(15);
            } else {
                alert("Geocode was not successful for the following reason: " + status);
            }
        });
    }

    this.getProviders = function(){
        $.ajax({
            type: "POST",
            url: "/providers/getAllProviders",
            success: function(data){
                // if index page adding values to filter
                // and binding functions to search
                if($("#provider_filter_select").length) {
                    $("#apply_filter_button").click(function () {
                        temp = $("#provider_filter_select option:selected").val();
                        _this.getPoints(temp)
                    });
                    var providers_comboBox = $("#provider_filter_select");
                    $.each(data, function (i, item) {
                        providers_comboBox.append('<option value="' + item.fields.name + '">' + item.fields.name + '</option>');
                    });
                    $("#search_form_points").keypress(function (e){
                        if (e.keyCode == 13) {
                            _this.codeAddress();
                        }
                    });
                    $("#search_form_points_button").click(function (){
                        _this.codeAddress();
                    });
                }
                _this.providers = data;
            },
            error: function(){
                alert('Error while trying to get providers list');
            }
        });
    }

    this.getPoints = function(provider){
        $.ajax({
            type: "POST",
            url: "/points/getAllPoints",
            data: {"provider" : provider},
            success: function (data) {
                var markers = [];
                $.each(data, function (i, item) {
                    var contentString = '<div class="content"><ul>' +
                        '<li>' + item.fields.name + '</li>' +
                        '<li>' + _this.providers[item.fields.provider-1].fields.name + '</li>' +
                        '<li><img src="/static/images/signal_strength/' + item.fields.average_signal +'.png"> </li>'+
                        '</ul></div>';
                    var latlng = new google.maps.LatLng(item.fields.coordinate_latitude,
                        item.fields.coordinate_longitude);
                    var infowindow = new google.maps.InfoWindow({
                        content: contentString
                    });
                    var marker = new google.maps.Marker({
                        position: latlng
                    });
                    markers.push(marker);
                    google.maps.event.addListener(marker, 'click', function () {
                        infowindow.open(_this.map, marker);
                    });
                });

                if (_this.markerClusterer != null) {
                    _this.markerClusterer.clearMarkers();
                }
                _this.markerClusterer = new MarkerClusterer(_this.map, markers, {
                    maxZoom: 13,
                    gridSize: 50,
                    styles: null
                });
            },
            error: function () {
                alert("Внутренняя ошибка");
            }
        });
    }

}


$().ready(function () {
    var map = new Map();
    map.init();

});

