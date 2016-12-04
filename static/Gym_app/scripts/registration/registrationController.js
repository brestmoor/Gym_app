/**
 * Created by Filip on 01.12.2016.
 */

registration
    .controller('registrationController', function ($http, $scope, $window) {
        $scope.submitForm = function () {
            $http({
                method: 'POST',
                url: '/users',
                data: $scope.form,
                headers: {'Content-Type': 'application/json'}
            }).then(function (response) {
                    if (response.status == 201)
                        $window.location.href = '/schedule';
                }, function (response) {
                    alert(response.data)
                }
            )
        };
    })
;