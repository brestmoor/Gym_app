/**
 * Created by Filip on 13.11.2016.
 */

schedule
    .directive('scheduleHead', function ($log) {
        return {
            template: '<th class="col-md-1 col-md-offset-1">#</th>' +
            '<th ng-repeat="(day, offset) in data.days track by $index" class="{{offset}}">{{day}}</th>'
        }
    });