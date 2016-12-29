session.service('loginService', ['$http', '$q', '$rootScope', function ($http, $q, $rootScope) {
    return {
        logIn: function (data) {
            return $q(function (resolve, reject) {
                $http({
                    method: 'POST',
                    url: '/session',
                    data: data,
                    headers: {'Content-Type': 'application/json'}
                }).then(function (response) {
                        var userData = angular.fromJson(response.data)
                        userData['isLoggedIn'] = true;
                        $rootScope.storage.userData = userData;
                        resolve(userData)
                    }, function (response) {
                        reject("Could not log in")
                    }
                );
            })
        },

        logOut: function () {
            $http.delete('/session')
                .then()
        }
    }
}]);