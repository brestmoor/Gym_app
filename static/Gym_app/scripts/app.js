/**
 * Created by Filip on 13.11.2016.
 */


var gymApp = angular.module('gymApp', ['schedule', 'personalTraining', 'ui.router', 'ngStorage']);

gymApp.config(function ($stateProvider, $urlRouterProvider, $httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

    $urlRouterProvider.otherwise('/schedule')

    $stateProvider
        .state('schedule', {
            url: '/schedule',
            templateUrl: '/static/Gym_app/views/schedule.html'
        })
        .state('register', {
            url: '/register',
            templateUrl: '/static/Gym_app/views/register.html'
        })
        .state('personalTraining', {
            url: '/personalTraining',
            templateUrl: '/static/Gym_app/views/personalTraining.html'
        })
        .state('personalTraining.schedule', {
            url: '/schedule',
            controller: 'personalTrainingScheduleCtrl',
            templateUrl: '/static/Gym_app/views/personalSchedule.html'
        })
})