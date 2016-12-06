/**
 * Created by Filip on 04.12.2016.
 */


schedule.controller('scheduleLoginCtrl', function (loginService) {
    var $ctrl = this;
    $ctrl.data = {};

    $ctrl.logIn = function () {
        loginService.logIn($ctrl.data)
        console.log($ctrl.data)
    };
    $ctrl.logOut = function () {
        sessionDataService.logOut()
    }
});
