angular.module('myApp').controller('AddEditFormController',
        function($scope, $location, $routeParams, Forms) {

    var id = $scope.id = $routeParams.id;
    if (id) {
      $scope.damnForm = Forms.get({ id : id });
    } else {
      $scope.damnForm = new Forms({ name: 'Sample', schema: [] });
    }

    $scope.save = function() {
      $scope.saving = true;
      if (typeof $scope.damnForm.labels === 'string') {
        $scope.damnForm.labels = $scope.damnForm.labels.split(',');
      }
      if (id) {
        $scope.damnForm.$update().then(function () {
            $location.path('/forms' + id + '/entries');
        }).finally(function() {
            $scope.saving = false;
        });
      } else {
        $scope.damnForm.$save().then(function () {
            $location.path('/');
        }).finally(function() {
            $scope.saving = false;
        });
      }
    };

    $scope.addField = function () {
      $scope.damnForm.schema = $scope.damnForm.schema || [];
      $scope.damnForm.schema.push({name: 'name', type:"string", mandatory: false});
    };

    $scope.removeField = function (index) {
      $scope.damnForm.schema.splice(index, 1);
    };

    $scope.fieldTypes = ['string', 'number', 'boolean', 'email', 'url', 'twitter', 'mobile'];
});
