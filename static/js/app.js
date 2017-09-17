var app = angular.module("myApp", ["ngRoute"]);

app.config(function($interpolateProvider, $httpProvider) {
  $interpolateProvider.startSymbol('[[');
  $interpolateProvider.endSymbol(']]');
  $httpProvider.defaults.xsrfCookieName = 'csrftoken';
  $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

});

app.config(function($routeProvider) {
    $routeProvider
    .when("/:id", {
        templateUrl : "/static/partials/home.html",
        controller:'product'
    })
});