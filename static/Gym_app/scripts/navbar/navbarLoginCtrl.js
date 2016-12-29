/**
 * Created by Filip on 19.12.2016.
 */



schedule.controller('navbarLoginCtrl', function ($scope, $localStorage, $rootScope, loginService) {
    $rootScope.storage = $localStorage.$default({
        userData: {
            isLoggedIn: false,
            name: '',
            lastName: '',
            email: '',
            group: '',
            isValidMember: false
        }
    })

    var $ctrl = this;
    $ctrl.data = {};


    $ctrl.logIn = function () {
        loginService.logIn($ctrl.data).then(function () {
        }, function (error) {
        })
    };
    $ctrl.logOut = function () {
        loginService.logOut()
    }
});
