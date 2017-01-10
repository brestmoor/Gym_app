/**
 * Created by Filip on 08.01.2017.
 */

trainerPersonalTraining.controller("trainerMemberCtrl", function ($scope, member, plans, diets, trainerMemberService, trainerMembersService) {

    $scope.member = member;
    $scope.plans = plans;
    $scope.diets = diets;

    $scope.colors = ['rgba(0, 165, 255, .8)', 'rgba(255, 165, 0, .8)', 'rgba(255, 0, 0, .9)'];

    $scope.labels = [];
    $scope.series = null;
    $scope.data = [
        []
    ];

    $scope.options = {
        limitLines: []
    };


    $scope.member.goal.records.forEach(function (record) {
        $scope.labels.push(record[1]);
        $scope.data[0].push(record[0])
    });

    for (var i = 0; i < $scope.member.goal.partialGoals.length; i++) {
        $scope.options.limitLines.push({
                label: 'cel ' + (i + 1).toString(),
                value: $scope.member.goal.partialGoals[i],
                color: i <= $scope.colors.length - 1 ? $scope.colors[i] : $scope.colors[$scope.colors.length - 1]
            }
        )
    }

    $scope.open = function ($event) {
        $event.preventDefault();
        $event.stopPropagation();

        $scope.opened = true;
    };

    $scope.addNewRecord = function () {
        $scope.labels.push($scope.newDate.toISOString().slice(0, 10));
        $scope.data[0].push($scope.newRecord);

        trainerMemberService.addNewRecord(member.data.id, {
            date: $scope.newDate.toISOString().slice(0, 10),
            value: $scope.newRecord
        })
    };

    $scope.addNewPartialGoal = function () {
        trainerMemberService.addPartialGoal(member.data.id, {
            value: $scope.newPartialGoal
        });

        $scope.options.limitLines.push({
                label: 'cel',
                value: $scope.newPartialGoal,
                color: 'rgba(0, 165, 255, .8)'
            }
        )
    };


    $scope.submit = function () {
        trainerMembersService.updateMember(member.data)
    }


    $scope.newDate = new Date();
    $scope.newRecord = 0;
    $scope.newPartialGoal = 0;

    $scope.dateOptions = {
        dateDisabled: false,
        formatYear: 'yy',
        maxDate: new Date(2020, 5, 22),
        minDate: new Date(2015, 5, 22),
        startingDay: 1
    };

    $scope.open2 = function () {
        $scope.popup2.opened = true;
    };

    $scope.popup2 = {
        opened: false
    };

}).service('trainerMemberService', ['$q', '$http', function ($q, $http) {
    this.addNewRecord = function (id, record) {
        return $q(function (resolve, reject) {
            $http.post('/members/' + id.toString() + '/records/', record).then(function (response) {
                resolve()
            }, function (errorResponse) {
                alert('Błąd');
                reject(angular.fromJson(errorResponse.data))
            })
        })
    }

    this.addPartialGoal = function (id, partialGoal) {
        return $q(function (resolve, reject) {
            $http.post('/members/' + id.toString() + '/partialGoals/', partialGoal).then(function (response) {
                resolve()
            }, function (errorResponse) {
                alert('Błąd');
                reject(angular.fromJson(errorResponse.data))
            })
        })
    }


}]);