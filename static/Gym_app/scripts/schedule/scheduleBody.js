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
            '<div class="panel-heading text-center">{{class.class_in_schedule.class_type.name}}</div>' +
            '<div class="panel-body text-center"><button type="button" ng-click="openDialog()">LALA</button></div>' +
            '</div>' +
            '</div>' +
            '</td>' +
            '</tr>'
        }
    });