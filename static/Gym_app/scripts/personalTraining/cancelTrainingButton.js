/**
 * Created by Filip on 27.12.2016.
 */

personalTraining.directive('cancelTrainingButton', function () {
    return {
        replace: true,
        template: '<button type="button" ng-show="storage.userData.isLoggedIn && storage.userData.isValidMember" class="btn btn-default">{{cancelButtonText}}</button>',
        link: function (scope, el, attrs) {
            scope.cancelButtonText = "Wypisz się";
            el.bind('click', function () {
                scope.cancelTraining(scope.training.id).then(function (response) {
                    console.log("wypisałem");
                    scope.training.attendee = null
                }, function () {
                    alert("Nie udalo sie wypisać")
                });
            })
        }
    }
})