


session.service('uiVersionService',['sessionDataService', 'userInformationService', function(sessionDataService, userInformationService) {
        var that = this;

        this.isLoggedIn = function () {
            return sessionDataService.getUserData() != null
        };
        this.isLoggedInAndValidMember = function () {
            return that.isLoggedIn() && userInformationService.isValid()
        };
        this.isLoggedInAndNotValidMember = function () {
            return that.isLoggedIn() && !userInformationService.isValid()
        }
    }]);