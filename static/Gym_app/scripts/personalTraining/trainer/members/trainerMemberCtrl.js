/**
 * Created by Filip on 08.01.2017.
 */

trainerPersonalTraining.controller("trainerMemberCtrl", function ($scope, member, plans, diets) {

    $scope.member = member;
    $scope.plans = plans;
    $scope.diets = diets;

    $scope.colors = ['rgba(0, 165, 255, .8)', 'rgba(255, 165, 0, .8)', 'rgba(255, 0, 0, .9)'];

    $scope.labels = [];
    $scope.series = null
    $scope.data = [
        []
    ];


    $scope.member.goal.records.forEach(function (record) {
        $scope.labels.push(record[1]);
        $scope.data[0].push(record[0])
    });


    $scope.options = {
        limitLines: []
    };

    for (var i = 0; i < $scope.member.goal.partialGoals.length; i++) {
        $scope.options.limitLines.push({
                label: 'cel ' + (i+1).toString(),
                value: $scope.member.goal.partialGoals[i],
                color: i <= $scope.colors.length-1 ? $scope.colors[i] : $scope.colors[$scope.colors.length-1]
            }
        )
    }

});