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
    }

    this.addMarker = function(location) {
        if (this.current_marker) {
            this.current_marker.setMap(null);
        }
        $("#id_coordinate_latitude").val(location.lat());
        $("#id_coordinate_longitude").val(location.lng());
        this.current_marker = new google.maps.Marker({
            position: location,
            map: _this.prototype.map,
            zIndex: 999
        });
    }
}


