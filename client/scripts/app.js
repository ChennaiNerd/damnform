//
// Starting point of the application
//
angular.module('myApp', [
    'ngRoute',
    'ngResource',
    'ngCookies',
    'ngSanitize',
    'ui.bootstrap'
    ])
    .config(function ($routeProvider) {
        $routeProvider
            .when('/', {
                templateUrl: 'scripts/views/forms/list.html',
                controller: 'ListFormsController'
            })
            .when('/forms/new', {
                templateUrl: 'scripts/views/forms/add.html',
                controller: 'AddEditFormController'
            })
            .when('/forms/:id/edit', {
                templateUrl: 'scripts/views/forms/edit.html',
                controller: 'AddEditFormController'
            })
            .when('/forms/:id/entries', {
                templateUrl: 'scripts/views/entries/list.html',
                controller: 'ListEntriesController'
            })
            .when('/forms/:formId/entries/:id', {
                templateUrl: 'scripts/views/entries/show.html',
                controller: 'ShowEntryController'
            })

            .otherwise({redirectTo: function() { return '/'; }});
    });

// angular.module('myApp')
//     .run(function($rootScope) {
//     });
