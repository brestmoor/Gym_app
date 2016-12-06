/**
 * Created by Filip on 04.12.2016.
 */


session.service('sessionDataService', function () {
    var userData = null;

    return {
        getUserData: function () {
            return userData;
        },

        setUserData: function (userDataInput) {
            userData = userDataInput;
        }
    }
});