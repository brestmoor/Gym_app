/**
 * Created by Filip on 08.01.2017.
 */


/**
 * Created by Filip on 06.01.2017.
 */


trainerPersonalTraining.service('trainerMembersService', ['$q', '$http', function ($q, $http) {
    this.getMembers = function (email) {
        return $q(function (resolve, reject) {
            $http.get('/members/?email=' + email).then(function (response) {
                resolve(angular.fromJson(response.data))
            }, function (errorResponse) {
                alert('Błąd');
                reject(angular.fromJson(errorResponse.data))
            })
        })
    };

    this.updateMember = function (memberObj) {
        return $q(function (resolve, reject) {
            $http.put('/members/', {member: memberObj}).then(function (response) {
                resolve()
            }, function (errorResponse) {
                alert('Błąd');
                reject(angular.fromJson(errorResponse.data))
            })
        })
    }

    this.getMember = function (id) {
        return $q(function (resolve, reject) {
            $http.get('/members/' + id).then(function (response) {
                resolve(angular.fromJson(response.data))
            }, function (errorResponse) {
                alert('Błąd');
                reject(angular.fromJson(errorResponse.data))
            })
        })
    };
}]);