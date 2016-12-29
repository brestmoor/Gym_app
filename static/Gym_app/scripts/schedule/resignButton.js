/**
 * Created by Filip on 11.12.2016.
 */


schedule.directive('resignButton', function () {
    return {
        replace: true,
        scope: {
            cancelClass: '&cancelClass',
            userClasses: '=userClasses',
            classId: '@classId',
            storage: '=storage',
            attendees: '=attendees'
        },
        template: '<button type="button" ng-show="storage.userData.isLoggedIn && storage.userData.isValidMember && doesBelongToUserClasses" class="btn btn-success" autofocus="true">{{resignButtonText}}</button>',
        link: function (scope, el, attrs) {
            scope.resignButtonText = "Wypisz się";
            scope.doesBelongToUserClasses = false;
            scope.$watchCollection('userClasses', function (newValue, oldValue) {
                if (newValue === undefined)
                    return;
                if (doesContain(newValue, Number(scope.classId))) {
                    scope.doesBelongToUserClasses = true;
                }
                else {
                    scope.doesBelongToUserClasses = false;
                }
            });
            el.bind('click', function () {
                scope.cancelClass().then(function (response) {
                    console.log("wypisuję");
                    scope.userClasses = response.data.classes;
                    scope.attendees = response.data.attendees
                }, function () {
                    alert("Nie udalo sie wypisać")
                });
            })
        }
    }
});