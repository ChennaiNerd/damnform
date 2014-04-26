angular.module('myApp').controller('ListFormsController',
        function($scope, Forms) {

    // Load students
    $scope.forms = Forms.query();
});
