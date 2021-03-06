/**
 * Created by Filip on 04.12.2016.
 */

schedule.directive('joinButton', function () {
    return {
        replace: true,
        scope: {
            joinClass: '&joinClass',
            userClasses: '=userClasses',
            classId: '@classId',
            storage: '=storage',
            attendees: '=attendees'
        },
        template: '<button type="button" ng-show="storage.userData.isLoggedIn && storage.userData.isValidMember && !doesBelongToUserClasses" class="btn btn-default">{{joinButtonText}}</button>',
        link: function (scope, el, attrs) {
            scope.joinButtonText = "Zapisz się";
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
                scope.joinClass().then(function (response) {
                    console.log("zapisuje");
                    scope.userClasses = response.data.classes;
                    scope.attendees = response.data.attendees
                }, function () {
                    alert("Nie udalo sie zapisac")
                });
            })
        }
    }
})