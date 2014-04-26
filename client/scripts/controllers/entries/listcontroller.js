angular.module('myApp').controller('ListEntriesController',
        function($scope, $location, $routeParams, Forms, Entries) {

    var id = $routeParams.id;
    var mandatories = $scope.mandatories = [];
    $scope.damnForm = Forms.get({ id : id }, function(damnForm) {
      for (var i = 0; i < damnForm.schema.length; i++ ) {
        if (damnForm.schema[i].mandatory) {
          mandatories.push(damnForm.schema[i].name);
        }
        console.log(mandatories);
      }
    });
    $scope.damnFormEntries = Entries.query({ formId : id });

    $scope.searchEntries = function (label) {
      if (label) {
        $scope.damnFormEntries = Entries.query({ formId : id, labels: label });
      } else if ($scope.search) {
        $scope.damnFormEntries = Entries.query({ formId : id, search: $scope.search });
      }
    }

    $scope.deleteForm = function () {
      if (!confirm('Are you sure to delete?')) {
        return;
      }
      $scope.damnForm.$delete().then(function () {
          $location.path('/');
      });
    }

});
