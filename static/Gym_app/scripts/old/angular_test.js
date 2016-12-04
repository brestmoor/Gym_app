/**
 * Created by Filip on 12.11.2016.
 */

angular.module('myApp', [])
    .directive('attrDirective', function ($log) {
        return {
            restrict: 'A',
            link: function (scope, el, attrs) {
                var incr = parseInt(attrs.incr || 1)
                    , val = 0;
                el.bind('click', function () {
                    el.html(val += incr);
                    $log.log(val);
                });
            }//el.bind do odpowiedniej funkcji ze scopa po wywolaniu starej?
        };
    });


angular.module('myApp', [])
    .directive('vectorText', function ($document) {
        return {
            template: '<span>{{heading}}</span>',
            link: function (scope, el, attrs) {
                el.css({
                    'float': 'left',
                    'padding': attrs.buffer + "px"
                });

                scope.heading = '';

                $document.on('mousemove', function (event) {
                    scope.$apply(function () {
                        if (event.pageY < 300) {
                            scope.heading = 'N';
                        }
                        else {
                            scope.heading = 'S';
                        }
                    });
                });
            }
        };
    });

angular.module('myApp', [])
    .controller('isoCtrl', function ($log, $scope, myValue, myService) {
        $scope.credentials = myValue;
        $scope.users = [
            'Alan',
            'Banksy',
            'Celina'
        ];
        $scope.text = "blablabla";
        $scope.outerval = 'siema';
        $scope.func = function () {
            $log.log("outer log")
        }
        $scope.swapName = function () {
            $scope.credentials.name = myService.getGreeting();
        };
    })
    .directive('iso', function ($log) {
        return {
            template: 'Inner: {{innerval}}',
            // scope: {
            //     innerval: '=myattr'
            // },
            link: function (scope) {
                scope.innerval = 'papa';
                scope.innerval = scope.credentials;
            }
        }
    })
    .value('myValue', {
        name: 'Tom',
        surname: 'Ford'
    })
    .service('myService', function () {
        var greeting = 'hi, service here';
        this.getGreeting = function () {
            return greeting
        }
    });