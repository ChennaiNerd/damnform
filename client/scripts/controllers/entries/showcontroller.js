angular.module('myApp').controller('ShowEntryController',
        function($scope, $rootScope, $routeParams, Entries) {

  var formId = $routeParams.formId;
  var id = $routeParams.id;
  $scope.damnFormEntry = Entries.get({ formId: formId, id : id });

});
