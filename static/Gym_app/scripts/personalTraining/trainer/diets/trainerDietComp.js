/**
 * Created by Filip on 08.01.2017.
 */


trainerPersonalTraining.component('trainerDietComp', {
    bindings: {
        diet: '<'
    },
    templateUrl: '/static/Gym_app/views/diet.html',
    controller: function () {
        this.days = ['Poniedziałek', 'Wtorek', 'Środa', 'Czwartek', 'Piątek', 'Sobota', 'Niedziela']
    }
})