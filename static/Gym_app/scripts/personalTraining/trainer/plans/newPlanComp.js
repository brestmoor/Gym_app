/**
 * Created by Filip on 07.01.2017.
 */

trainerPersonalTraining.component('newPlanComp', {
    bindings: {
        exercises: '<',
        planName: '<'
    },
    templateUrl: '/static/Gym_app/views/trainer/plans/newPlan.html',
    controller: function (trainerPlansService, $rootScope, $state) {
        this.days = ['Poniedziałek', 'Wtorek', 'Środa', 'Czwartek', 'Piątek', 'Sobota', 'Niedziela'];
        this.plannedMeals = [];
        this.addNewExercise = function (day, order) {
            this.plannedMeals.push({
                day: day,
                exercise: null,
                order: order,
                repetitions: ''
            })
        };
        this.createNew = function () {
            trainerPlansService.createPlan(this.plannedMeals, this.planName, $rootScope.storage.userData.email)
                .then(function (response) {
                $state.transitionTo('trainerPersonalTraining.plans');
            })
        }
    }
});