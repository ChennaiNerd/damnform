angular.module('myApp').controller('ListEntriesController',
        function($scope, $location, $routeParams, Forms, Entries, ngDialog) {

    $scope.currentLabel = 'All';
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
    $scope.damnFormEntries = Entries.query({ form_id : id });

    $scope.searchEntries = function (label) {
      if (label) {
        $scope.currentLabel = label;
        $scope.damnFormEntries = Entries.query({ form_id : id, labels: label });
      } else if ($scope.search) {
        $scope.currentLabel = 'All';
        $scope.damnFormEntries = Entries.query({ form_id : id, search: $scope.search });
      } else {
        $scope.currentLabel = 'All';
        $scope.damnFormEntries = Entries.query({ form_id : id });
      }
    }

    $scope.isCurrentLabel = function (label) {
      return $scope.currentLabel === label;
    }

    $scope.editLabels = function (entry) {
      var labels = prompt("Please edit labels", entry.labels || '');
      if (labels != null) {
        entry.labels = labels;
        entry.$update();
      }
    }

    $scope.showEntry = function (entry) {
      var newScope = $scope.$new();
      newScope.entry = entry;
      ngDialog.open({
          template: 'scripts/views/entries/show.html',
          className: 'ngdialog-theme-default ngdialog-theme-custom',
          scope: newScope
        });
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
