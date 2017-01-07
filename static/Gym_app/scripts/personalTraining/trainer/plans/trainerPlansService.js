/**
 * Created by Filip on 06.01.2017.
 */


trainerPersonalTraining.service('trainerPlansService', ['$q', '$http', function ($q, $http) {
    this.getPlans = function () {
        return $q(function (resolve, reject) {
            $http.get('/trainingPlans').then(function (response) {
                resolve(angular.fromJson(response.data))
            }, function (errorResponse) {
                alert('Błąd');
                reject(angular.fromJson(errorResponse.data))
            })
        })
    };

    this.getPlan = function (id) {
        return $q(function (resolve, reject) {
            $http.get('/trainingPlans/' + id).then(function (response) {
                resolve(angular.fromJson(response.data))
            }, function (errorResponse) {
                alert('Błąd');
                reject(angular.fromJson(errorResponse.data))
            })
        })
    };

    this.deletePlan = function (id) {
        return $q(function (resolve, reject) {
            $http.delete('/trainingPlans/' + id).then(function (response) {
                resolve(angular.fromJson(response.data))
            }, function (errorResponse) {
                alert('Błąd');
                reject(angular.fromJson(errorResponse.data))
            })
        })
    };

    this.getExercises = function () {
        return $q(function (resolve, reject) {
            $http.get('/exercises/').then(function (response) {
                resolve(angular.fromJson(response.data))
            }, function (errorResponse) {
                alert('Błąd');
                reject(angular.fromJson(errorResponse.data))
            })
        })
    };

    this.createPlan = function (plan, planName, email) {
        var data = {
            plan: plan,
            planName: planName,
            email: email
        };
        return $q(function (resolve, reject) {
            $http.post('/trainingPlans/', data).then(function (response) {
                resolve()
            }, function (errorResponse) {
                alert('Błąd');
                reject(angular.fromJson(errorResponse.data))
            })
        })
    };
}]);