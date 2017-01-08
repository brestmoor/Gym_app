/**
 * Created by Filip on 08.01.2017.
 */

/**
 * Created by Filip on 31.12.2016.
 */

trainerPersonalTraining.component('trainerMembersComp', {
    bindings: {
        members : '<',
        plans: '<',
        diets: '<'
    },
    templateUrl : '/static/Gym_app/views/trainer/members/trainerMembers.html',
    controller: function (trainerMembersService, $rootScope) {
        this.trainerEmail = $rootScope.storage.userData.email;
        var that = this;

        this.submit = function (member) {
            trainerMembersService.updateMember(member)
        }
    }
});