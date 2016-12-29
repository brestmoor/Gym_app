/**
 * Created by Filip on 26.12.2016.
 */


personalTraining.directive('joinTrainingButton', function () {
    return {
        replace: true,
        template: '<button type="button" ng-show="storage.userData.isLoggedIn && storage.userData.isValidMember" class="btn btn-default">{{joinButtonText}}</button>',
        link: function (scope, el, attrs) {
            scope.joinButtonText = "Zapisz się";
            el.bind('click', function () {
                scope.joinTraining(scope.training.id).then(function (response) {
                    console.log("zapisuje");
                    scope.training.attendee = response.data
                }, function () {
                    alert("Nie udalo sie zapisac")
                });
            })
        }
    }
});