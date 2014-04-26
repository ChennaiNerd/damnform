angular.module('myApp').controller('ListFormsController',
        function($scope, Forms) {

    // Load forms
    $scope.damnForms = Forms.query();
});
