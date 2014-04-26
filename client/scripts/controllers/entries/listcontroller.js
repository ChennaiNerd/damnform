angular.module('myApp').controller('ListEntriesController',
        function($scope, $rootScope, $routeParams, Forms, Entries) {

    var id = $routeParams.id;
    var mandatories = $scope.mandatories = [];
    $scope.damnForm = Forms.get({ id : id });
    $scope.damnFormEntries = Entries.query({ formId : id }, function(entries) {
      for (var i = 0; i < entries.schema.length; i++ ) {
        if (entries.schema[i].mandatory) {
          mandatories.push(entries.schema[i].name);
        }
        console.log(mandatories);
      }
    });

});
