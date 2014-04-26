angular.module('myApp').controller('AddFormController',
        function($scope, $location, Forms) {

    var damnForm = new Forms({ name: 'Sample', schema: [] });
    $scope.damnForm = damnForm;

    $scope.save = function() {
        $scope.saving = true;
        damnForm.$save().then(function () {
            $location.path('/');
        }).finally(function() {
            $scope.saving = false;
        });
    };

    $scope.addField = function () {
        $scope.damnForm.schema.push({name: 'Name', type:"string", mandatory: false});
    };

    $scope.removeField = function (index) {
        $scope.damnForm.schema.splice(index, 1);
    };
});
