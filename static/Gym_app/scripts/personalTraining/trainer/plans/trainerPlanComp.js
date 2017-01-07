/**
 * Created by Filip on 06.01.2017.
 */


trainerPersonalTraining.component('trainerPlanComp', {
    bindings: {
        plan: '<'
    },
    templateUrl: '/static/Gym_app/views/plan.html',
    controller: function () {
        this.days = ['Poniedziałek', 'Wtorek', 'Środa', 'Czwartek', 'Piątek', 'Sobota', 'Niedziela']
    }
})