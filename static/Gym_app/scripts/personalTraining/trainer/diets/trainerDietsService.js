/**
 * Created by Filip on 07.01.2017.
 */
/**
 * Created by Filip on 06.01.2017.
 */


trainerPersonalTraining.service('trainerDietsService', ['$q', '$http', function ($q, $http) {
    this.getDiets = function (email) {
        return $q(function (resolve, reject) {
            $http.get('/diets/?email=' + email).then(function (response) {
                resolve(angular.fromJson(response.data))
            }, function (errorResponse) {
                alert('Błąd');
                reject(angular.fromJson(errorResponse.data))
            })
        })
    };

    this.getDiet = function (id) {
        return $q(function (resolve, reject) {
            $http.get('/diets/' + id).then(function (response) {
                resolve(angular.fromJson(response.data))
            }, function (errorResponse) {
                alert('Błąd');
                reject(angular.fromJson(errorResponse.data))
            })
        })
    };

    this.deleteDiet = function (id) {
        return $q(function (resolve, reject) {
            $http.delete('/diets/' + id).then(function (response) {
                resolve(angular.fromJson(response.data))
            }, function (errorResponse) {
                alert('Błąd');
                reject(angular.fromJson(errorResponse.data))
            })
        })
    };

    this.getMeals = function () {
        return $q(function (resolve, reject) {
            $http.get('/meals/').then(function (response) {
                resolve(angular.fromJson(response.data))
            }, function (errorResponse) {
                alert('Błąd');
                reject(angular.fromJson(errorResponse.data))
            })
        })
    };

    this.createDiet = function (diet, dietName, email) {
        var data = {
            diet: diet,
            dietName: dietName,
            email: email
        };
        return $q(function (resolve, reject) {
            $http.post('/diets/', data).then(function (response) {
                resolve()
            }, function (errorResponse) {
                alert('Błąd');
                reject(angular.fromJson(errorResponse.data))
            })
        })
    };
}]);