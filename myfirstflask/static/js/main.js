(function () {
    'use strict';
    var defaultOptions, map, controlMap, openstreetmap, googleHybrid;
    //configuração padrão do mapa
    defaultOptions = {zoom: 19, center: [-13.0015785, -38.507568], zoomControl: true};
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
}());
