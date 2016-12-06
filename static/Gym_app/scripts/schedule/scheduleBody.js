/**
 * Created by Filip on 13.11.2016.
 */

schedule
    .directive('scheduleBody', function ($log) {
        return {
            template: '<tr ng-repeat="(hour, list) in data.classes">' +
            '<td>{{hour}}</td>' +
            '<td ng-repeat="class in list track by $index" class="col-md-1">' +
                '<div ng-if="class != null ">' +
                    '<div class="panel panel-default">' +
                        '<div class="panel-heading text-center">{{class.class_in_schedule.class_type.name}}' +
                        '</div>' +
                        '<div class="panel-body text-center">' +
                            '<button type="button" ng-show="!uiVersionService.isLoggedIn()" class="btn btn-default" ng-click="openLoginDialog()">Zaloguj się</button>' +
                            '<button type="button" ng-show="uiVersionService.isLoggedInAndValidMember()" class="btn btn-default" ng-click="joinClass()">Zapisz się</button>' +
                            '<button type="button" ng-show="uiVersionService.isLoggedInAndNotValidMember()" class="btn btn-default disabled" ng-click="openLoginDialog()">Nie posiadasz ważnego karnetu</button>' +
                        '</div>' +
                    '</div>' +
                '</div>' +
            '</td>' +
            '</tr>'
        }
    });