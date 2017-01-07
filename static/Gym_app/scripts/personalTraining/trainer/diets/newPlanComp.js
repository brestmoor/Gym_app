/**
 * Created by Filip on 07.01.2017.
 */

trainerPersonalTraining.component('newDietComp', {
    bindings: {
        dietName: '<'
    },
    templateUrl: '/static/Gym_app/views/trainer/diets/newDiet.html',
    controller: function (trainerDietsService, $rootScope, $state, $watch) {
        this.days = ['Poniedziałek', 'Wtorek', 'Środa', 'Czwartek', 'Piątek', 'Sobota', 'Niedziela'];
        this.plannedMeals = [];
        this.mealsByDay = {
            Poniedziałek: [],
            Wtorek: [],
            Środa: [],
            Czwartek: [],
            Piątek: [],
            Sobota: [],
            Niedziela: []
        }
        this.caloriesByDay = {
            Poniedziałek: 0,
            Wtorek: 0,
            Środa: 0,
            Czwartek: 0,
            Piątek: 0,
            Sobota: 0,
            Niedziela: 0
        }

        this.$watch(function (scope) {
            return scope.mealsByDay['Poniedziałek']
        }, function (newValue, oldValue) {
            this.caloriesByDay['Poniedziałek'] = this.recalculateCalories('Poniedziałek')
        }, true);


        this.$watch(function (scope) {
            return scope.mealsByDay['Wtorek']
        }, function (newValue, oldValue) {
            this.caloriesByDay['Wtorek'] = this.recalculateCalories('Wtorek')
        }, true);

        this.$watch(function (scope) {
            return scope.mealsByDay['Środa']
        }, function (newValue, oldValue) {
            this.caloriesByDay['Środa'] = this.recalculateCalories('Środa')
        }, true);

        this.$watch(function (scope) {
            return scope.mealsByDay['Czwartek']
        }, function (newValue, oldValue) {
            this.caloriesByDay['Czwartek'] = this.recalculateCalories('Czwartek')
        }, true);

        this.$watch(function (scope) {
            return scope.mealsByDay['Piątek']
        }, function (newValue, oldValue) {
            this.caloriesByDay['Piątek'] = this.recalculateCalories('Piątek')
        }, true);

        this.$watch(function (scope) {
            return scope.mealsByDay['Sobota']
        }, function (newValue, oldValue) {
            this.caloriesByDay['Sobota'] = this.recalculateCalories('Sobota')
        }, true);

        this.$watch(function (scope) {
            return scope.mealsByDay['Niedziela']
        }, function (newValue, oldValue) {
            this.caloriesByDay['Niedziela'] = this.recalculateCalories('Niedziela')
        }, true);

        this.recalculateCalories = function (nameOfTheDay) {
            var sum = 0;
            mealsByDay[nameOfTheDay].forEach(function (entry) {
                sum = sum + entry.calories;
            });
            return sum
        };

        this.addNewMeal = function (day, order) {
            var newMeal = {
                day: day,
                name: '',
                order: order,
                quantity: ''
            };
            this.assignMealToDay(newMeal);
            this.plannedMeals.push(newMeal)
        };

        this.assignMealToDay = function (meal) {
            this.mealsByDay[meal.day].push(meal)
        };

        this.createNew = function () {
            trainerDietsService.createDiet(this.plannedMeals, this.dietName, $rootScope.storage.userData.email)
                .then(function (response) {
                    $state.transitionTo('trainerPersonalTraining.diets');
                })
        }
    }
});