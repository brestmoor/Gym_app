/**
 * Created by Filip on 04.12.2016.
 */


session.controller('loginCtrl', function ($http) {
    var $ctrl = this;
    $ctrl.data = {};

    $ctrl.logIn = function (){
        $http.post('/session', data)
            .then(function (response) {

            })

    }
});