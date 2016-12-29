/**
 * Created by Filip on 13.11.2016.
 */

schedule
    .directive('scheduleHead', function ($log) {
        return {
            template: '<th class="hour">godz.</th>' +
            '<th ng-repeat="day in commonData.days track by $index" class="day-name">{{day}}</th>'
        }
    });