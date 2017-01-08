/**
 * Created by Filip on 07.01.2017.
 */

trainerPersonalTraining.component('newDietComp', {
    bindings: {
        dietName: '<'
    },
    templateUrl: '/static/Gym_app/views/trainer/diets/newDiet.html',
    controller: function (trainerDietsService, $rootScope, $state) {
        this.days = ['Poniedziałek', 'Wtorek', 'Środa', 'Czwartek', 'Piątek', 'Sobota', 'Niedziela'];
        this.plannedMeals = [];
        this.addNewMeal = function (day, order) {
            this.plannedMeals.push({
                day: day,
                name: '',
                calories: 0,
                order: order,
                quantity: 0
            })
        };
        this.createNew = function () {
            trainerDietsService.createDiet(this.plannedMeals, this.dietName, $rootScope.storage.userData.email)
                .then(function (response) {
                    $state.transitionTo('trainerPersonalTraining.diets', {email: $rootScope.storage.userData.email});
                })
        }
    }
});