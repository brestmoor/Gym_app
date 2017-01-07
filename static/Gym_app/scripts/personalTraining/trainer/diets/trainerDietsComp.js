/**
 * Created by Filip on 07.01.2017.
 */
/**
 * Created by Filip on 31.12.2016.
 */

trainerPersonalTraining.component('trainerDietsComp', {
    bindings: {
        diets : '<'
    },
    templateUrl : '/static/Gym_app/views/trainer/diets/trainerDiets.html',
    controller: function (trainerDietsService) {
        var that = this;

        that.deleteDiet = function (id) {
            trainerDietsService.deleteDiet(id).then(function (response) {
                var index = that.findDietById(that.diets, id);
                that.diets.splice(index, 1);
            })
        };

        that.findDietById = function (diet, id) {
            for (var i=0; i<diet.length; i++){
                if(diet[i].id === id)
                    return i;
            }
        }
    }
});