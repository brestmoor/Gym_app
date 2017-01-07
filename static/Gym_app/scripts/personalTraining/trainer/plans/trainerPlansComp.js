/**
 * Created by Filip on 31.12.2016.
 */

trainerPersonalTraining.component('trainerPlansComp', {
    bindings: {
        plans : '<'
    },
    templateUrl : '/static/Gym_app/views/trainer/plans/trainerPlans.html',
    controller: function (trainerPlansService) {
        var that = this;

        that.deletePlan = function (id) {
            trainerPlansService.deletePlan(id).then(function (response) {
                var index = that.findDietById(that.plans, id);
                that.plans.splice(index, 1);
            })
        };

        that.findDietById = function (plan, id) {
            for (var i=0; i<plan.length; i++){
                if(plan[i].id === id)
                    return i;
            }
        }
    }
});