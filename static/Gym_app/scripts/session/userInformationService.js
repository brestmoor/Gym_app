/**
 * Created by Filip on 06.12.2016.
 */


session.service('userInformationService', function () {
    var isValidMember = false;

    return {
        setValidMember: function (isValid) {
            isValidMember = isValid;
        },

        isValid: function () {
            return isValidMember;
        }
    }
})