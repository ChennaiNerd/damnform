angular.module('myApp').controller('ListEntriesController',
        function($scope, $location, $routeParams, Forms, Entries, Mails, ngDialog) {

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
        if (typeof labels === 'string') {
          entry.labels = labels.split(',');
        } else {
          entry.labels = labels;
        }
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

    $scope.sendingmail = false;
    $scope.sendMail = function (to) {
      $scope.sendingmail = true;
      if (to) {
        $scope.to = [to];
      } else {
        //Get all to
        var to = $scope.to = [];
        for (var i = 0; i < $scope.damnFormEntries.length; i++) {
          to.push($scope.damnFormEntries[i].email);
        }
      }
    }

    $scope.cancelMail = function () {
      $scope.sendingmail = false;
    }

    $scope.sendMails = function() {
      var mails = new Mails({ form_id: { '$oid' : id } });
      mails.to = $scope.to;
      mails.subject = $scope.mailSubject;
      mails.message = $scope.mailMessage;
      mails.$save().then(function() {
        $scope.mailSubject = '';
        $scope.mailMessage = '';
        $scope.sendingmail = false;
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
