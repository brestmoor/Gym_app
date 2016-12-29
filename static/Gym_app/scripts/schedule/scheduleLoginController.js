/**
 * Created by Filip on 04.12.2016.
 */


schedule.controller('scheduleLoginCtrl', function ($scope, loginService) {
    var $ctrl = this;
    $ctrl.data = {};

    $ctrl.logIn = function () {
        loginService.logIn($ctrl.data).then(function () {
            alert('ok')
        }, function (error) {
            alert(error)
        })
    };
    $ctrl.logOut = function () {
        loginService.logOut()
    }
});
