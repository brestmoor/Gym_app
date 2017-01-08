/**
 * Created by Filip on 08.01.2017.
 */

trainerPersonalTraining.component('trainerMemberComp', {
    bindings: {
        member: '<',
        plans: '<',
        diets: '<'
    },

    templateUrl: '/static/Gym_app/views/trainer/members/member.html',
    controller: function (trainerMembersService) {
        var that = this;
        // this.$onInit = function () {
        //     this.addAchievements(this.memberId, this.achievements)
        // };
    }
});