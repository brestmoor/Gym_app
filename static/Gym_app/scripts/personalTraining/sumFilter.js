/**
 * Created by Filip on 07.01.2017.
 */
gymApp.filter('sumCalories', function () {
    return function (data) {
        if (typeof(data) === 'undefined') {
            return 0;
        }

        var sum = 0;
        for (var i = data.length - 1; i >= 0; i--) {
            var tempSum = parseInt(data[i].calories);
            if (isNaN(tempSum)) {
                tempSum = 0;
            }
            sum += tempSum
        }

        return sum;
    };
});