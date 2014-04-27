angular.module('myApp').controller('ShowEntryController',
        function($scope, $rootScope, $routeParams, Entries) {

  var form_id = $routeParams.form_id;
  var id = $routeParams.id;
  $scope.damnFormEntry = Entries.get({ form_id: form_id, id : id });

});
