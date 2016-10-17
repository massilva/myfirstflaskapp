(function () {
    'use strict';
    var defaultOptions, map, options;
    options = {
        enableHighAccuracy: true,
        timeout: 5000,
        maximumAge: 0
    };
    //configuração padrão do mapa
    defaultOptions = {zoom: 19, center: [-13.0035168, -38.4802806], zoomControl: true};
    // Carregar mapa
    function loadMap(defaultOptions) {
        var controlMap, openstreetmap, googleHybrid, promise;
        //controle de camadas
        controlMap = L.control.layers();
        // Base de mapas - ruas
        openstreetmap = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            maxZoom: 19,
            minZoom: 1,
            attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors <a href="https://www.rnp.br" target="_blank">RNP</a>'
        });
        // Base de mapas - híbrido do google
        googleHybrid = L.tileLayer('http://{s}.google.com/vt/lyrs=s,h&x={x}&y={y}&z={z}', {
            maxZoom: 20,
            subdomains: ['mt0', 'mt1', 'mt2', 'mt3']
        });
        // Adiciona a base de mapas ao controle
        controlMap.addBaseLayer(openstreetmap, "Ruas");
        controlMap.addBaseLayer(googleHybrid, "Satélite");
        // Instância o mapa
        map = L.map('map', defaultOptions);
        // Base de mapa padrão
        map.addLayer(googleHybrid);
        // Adiciona controle de base de mapas
        map.addControl(controlMap);
        map.on("click", function (e) {
            var data, promiseAdd;
            data = {
                lat: e.latlng.lat,
                lng: e.latlng.lng
            };
            promiseAdd = $.post("/marker/add", data);
            promiseAdd.done(function (response) {
                var latlng;
                response = JSON.parse(response);
                latlng = L.latLng(response.lat, response.lng);
                L.marker(latlng).addTo(this);
            }.bind(this));
        });
        promise = $.get("/marker/all");
        promise.done(function (response) {
            response = JSON.parse(response);
            response.map(function (coord) {
                L.marker(coord).addTo(map);
            });
        });
    }
    // Callback sucesso geolocalização
    function successGeo(position) {
        defaultOptions.center = [position.coords.latitude, position.coords.longitude];
        if (!map) {
            loadMap(defaultOptions);
        } else {
            map.panTo(defaultOptions.center);
        }
    }
    // Callback erro geolocalização
    function errorGeo(err) {
        console.warn('ERROR(' + err.code + '): ' + err.message);
    }
    // Geolocation support
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(successGeo, errorGeo, options);
    } else {
        alert("Geolocation is not supported by this browser.");
    }
    loadMap(defaultOptions);

}());
