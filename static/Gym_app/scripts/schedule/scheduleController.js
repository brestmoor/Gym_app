/**
 * Created by Filip on 13.11.2016.
 */

schedule
    .controller('scheduleController', function ($http, $scope, $log, $localStorage, $rootScope, daysOfTheWeekProvider, offsetService, loginModalService, classAttendanceService, usersClassesService) {
        $scope.data = {};

        daysOfTheWeekProvider.getDaysOfTheWeek();

        $http.get('http://localhost:8000/schedule/classes')
            .then(function (response) {
                $scope.data.classes = angular.fromJson(response.data);
            });



        $scope.$watch(function (scope) {
            return scope.storage.userData.isLoggedIn;
        }, function (isLoggedIn) {
            if (isLoggedIn == true) {
                $scope.userClasses = [];
                usersClassesService.getClassesIds().then(function (classes) {
                    $scope.userClasses = classes
                }, function (error) {
                    alert(error)
                })
            }
        });

        $scope.openLoginDialog = loginModalService.open;
        $scope.joinClass = classAttendanceService.join;
        $scope.cancelClass = classAttendanceService.cancel;

    })
    .service('offsetService', function () {
        this.addOffset = function (days) {
            daysDict = {};
            for (i = 0; i < days.length; i++) {
                daysDict[days[i]] = (i == 6 ? "col-md-1 col-md-offset-2" : "col-md-1")
            }
            return daysDict
        }
    })
    .service('classAttendanceService', ['$http', '$q', function ($http, $q) {
        this.join = function (classNumber) {
            return $q(function (resolve, reject) {
                $http.post('/schedule/classes/' + classNumber + '/attendees', '').then(function (response) {
                        resolve(response)
                    }, function (response) {
                        reject(response)
                    }
                )
            })
        }

        this.cancel = function (classNumber) {
            return $q(function (resolve, reject) {
                $http.delete('/schedule/classes/' + classNumber + '/attendees', '').then(function (response) {
                        resolve(response)
                    }, function (response) {
                        reject(response)
                    }
                )
            })
        }
    }])
    .service('loginModalService', ['$uibModal', function (uibModal) {
        this.open = function () {
            var modelInstance = uibModal.open({
                templateUrl: '/static/Gym_app/views/modalLogin.html'
            })
        };
    }])
    .service('usersClassesService', ['$http', '$q', function ($http, $q) {
        this.getClasses = function () {
            return $q(function (resolve, reject) {
                $http.get('/member/classes').then(function (response) {
                    resolve(angular.fromJson(response.data))
                }, function (errorResponse) {
                    reject(angular.fromJson(errorResponse.data))
                })
            })
        }

        this.getClassesIds = function () {
            return $q(function (resolve, reject) {
                $http.get('/member/classes/?q=ids').then(function (response) {
                    resolve(angular.fromJson(response.data))
                }, function (errorResponse) {
                    reject(angular.fromJson(errorResponse.data))
                })
            })
        }
    }])
    .service('daysOfTheWeekProvider', ['$http', '$rootScope', function ($http, $rootScope) {
        this.getDaysOfTheWeek = function () {
            $http.get('http://localhost:8000/schedule/days')
                .then(function (response) {
                    $rootScope.commonData = {};
                    $rootScope.commonData.days = angular.fromJson(response.data);
                })
        };
    }]);
