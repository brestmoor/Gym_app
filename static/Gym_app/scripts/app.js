/**
 * Created by Filip on 13.11.2016.
 */


var gymApp = angular.module('gymApp', ['schedule', 'personalTraining',
    'ui.router', 'ngStorage', 'ngSanitize', 'trainerPersonalTraining', 'chart.js']);

gymApp.config(function ($stateProvider, $urlRouterProvider, $httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

    $urlRouterProvider.otherwise('/schedule');

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
        .state('trainerPersonalTraining', {
            url: '/trainerPersonalTraining',
            templateUrl: '/static/Gym_app/views/trainer/trainerPersonalTraining.html'
        })
        .state('trainerPersonalTraining.plans', {
            url: '/plans',
            component: 'trainerPlansComp',
            resolve: {
                plans: function (trainerPlansService, $transition$) {
                    return trainerPlansService.getPlans()
                }
            }
        })
        .state('trainerPersonalTraining.diets', {
            url: '/diets/{email}',
            component: 'trainerDietsComp',
            resolve: {
                diets: function (trainerDietsService, $transition$) {
                    return trainerDietsService.getDiets($transition$.params().email)
                }
            }
        })
        .state('trainerPersonalTraining.members', {
            url: '/members/{email}',
            component: 'trainerMembersComp',
            resolve: {
                members: function (trainerMembersService, $transition$) {
                    return trainerMembersService.getMembers($transition$.params().email)
                },
                diets: function (trainerDietsService, $transition$) {
                    return trainerDietsService.getDiets($transition$.params().email)
                },
                plans: function (trainerPlansService, $transition$) {
                    return trainerPlansService.getPlans()
                }
            }
        })
        .state('trainerPersonalTraining.trainingPlan', {
            url: '/trainerPersonalTraining/plans/{planId}',
            component: 'trainerPlanComp',
            resolve: {
                plan: function (trainerPlansService, $transition$) {
                    return trainerPlansService.getPlan($transition$.params().planId);
                }
            }
        })
        .state('trainerPersonalTraining.newTrainingPlan', {
            url: '/trainerPersonalTraining/plans/new/{planName}',
            component: 'newPlanComp',
            resolve: {
                exercises: function (trainerPlansService) {
                    return trainerPlansService.getExercises();
                },
                planName: function ($transition$) {
                    return $transition$.params().planName
                }
            }
        })
        .state('trainerPersonalTraining.diet', {
            url: '/trainerPersonalTraining/diets/{dietId}',
            component: 'trainerDietComp',
            resolve: {
                diet: function (trainerDietsService, $transition$) {
                    return trainerDietsService.getDiet($transition$.params().dietId);
                }
            }
        })
        .state('trainerPersonalTraining.newDiet', {
            url: '/trainerPersonalTraining/diets/new/{dietName}',
            component: 'newDietComp',
            resolve: {
                dietName: function ($transition$) {
                    return $transition$.params().dietName
                }
            }
        })
        .state('trainerPersonalTraining.member', {
            url: '/trainerPersonalTraining/members/{email}/trainer/{memberId}',
            controller: 'trainerMemberCtrl',
            templateUrl: '/static/Gym_app/views/trainer/members/member.html',
            resolve: {
                member: function (trainerMembersService, $transition$) {
                    return trainerMembersService.getMember($transition$.params().memberId);
                },
                diets: function (trainerDietsService, $transition$) {
                    return trainerDietsService.getDiets($transition$.params().email)
                },
                plans: function (trainerPlansService, $transition$) {
                    return trainerPlansService.getPlans()
                }
            }
        })
})