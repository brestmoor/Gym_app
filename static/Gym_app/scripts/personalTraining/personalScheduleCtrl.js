/**
 * Created by Filip on 24.12.2016.
 */

personalTraining.controller('personalTrainingScheduleCtrl', function ($scope, $rootScope,
                                                                      $http, daysOfTheWeekProvider, trainingAttendanceService) {
    if (angular.equals($rootScope.commonData, undefined) || angular.equals($rootScope.commonData.days, {})) {
        daysOfTheWeekProvider.getDaysOfTheWeek();
    }
    $scope.data = {};
    $http.get('/personalTraining/trainings').then(function (response) {
        $scope.data.trainings = response.data;
    }, function (response) {
        alert('error' + response.data)
    })

    $scope.joinTraining = trainingAttendanceService.joinTraining;
    $scope.cancelTraining = trainingAttendanceService.cancelTraining;

}).service('trainingAttendanceService', ['$http', '$q', function ($http, $q) {
    this.joinTraining = function (classNumber) {
        return $q(function (resolve, reject) {
            $http.post('/personalTraining/trainings/' + classNumber + '/attendee').then(function (response) {
                resolve(response)
            }, function (error) {
                reject(error)
            })
        })
    };

    this.cancelTraining = function (classNumber) {
        return $q(function (resolve, reject) {
            $http.delete('/personalTraining/trainings/' + classNumber + '/attendee').then(function (response) {
                resolve(response)
            }, function (error) {
                reject(error)
            })
        })
    }

}])