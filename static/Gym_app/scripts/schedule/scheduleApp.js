/**
 * Created by Filip on 15.11.2016.
 */
var schedule = angular.module('schedule', ['ngRoute', 'registration']);
schedule.config(function ($routeProvider) {
    $routeProvider
        .when("/register", {
            templateUrl: "/static/Gym_app/views/register.html"
        }).when("/", {
        templateUrl: "/static/Gym_app/views/schedule.html"
    })
});