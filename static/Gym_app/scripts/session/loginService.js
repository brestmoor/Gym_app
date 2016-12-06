

session.service('loginService',
    ['$http', 'sessionDataService', 'userInformationService', function ($http, sessionDataService, userInformationService) {
    var setSession = function (response) {
        sessionDataService.setUserData()
    };

    var invalidate = function () {
        sessionDataService.setUserData(null); //todo dolozyc pakowanie info z userInfoServ
    };

    return {
        logIn: function (data) {
            $http({
                method: 'POST',
                url: '/session',
                data: data,
                headers: {'Content-Type': 'application/json'}
            }).then(function (response) {
                    setSession(angular.fromJson(response.data))
                });
            console.log(data)
        },

        logOut: function () {
            $http.delete('/session')
                .then(invalidate())
        }
    }
}])