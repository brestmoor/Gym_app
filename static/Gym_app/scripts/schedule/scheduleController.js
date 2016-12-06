/**
 * Created by Filip on 13.11.2016.
 */

schedule
    .controller('scheduleController', function ($http, $scope, $log, offsetService, loginModalService, uiVersionService, joinClassService) {
        $scope.data = {};
        $http.get('http://localhost:8000/schedule/days')
            .then(function (response) {
                $scope.data.days = offsetService.addOffset(angular.fromJson(response.data));
            });

        $http.get('http://localhost:8000/schedule/classes')
            .then(function (response) {
                $scope.data.classes = angular.fromJson(response.data);
            })

        $scope.openLoginDialog = loginModalService.open;
        $scope.joinClass = joinClassService.join();

        $scope.uiVersionService = uiVersionService;

    })
    .service('offsetService', function () {
        this.addOffset = function (days) {
            daysDict = {};
            for (i = 0; i < days.length; i++) {
                daysDict[days[i]] = i == 6 ? "col-md-1 col-md-offset-1" : "col-md-1"
            }
            return daysDict
        }
    })
    .service('joinClassService', function () {
        this.join = function () {

        }
    })
    .service('loginModalService', ['$uibModal', function (uibModal) {
        this.open = function () {
            var modelInstance = uibModal.open({
                templateUrl: '/static/Gym_app/views/modalLogin.html'
            })
        };
    }])


;
