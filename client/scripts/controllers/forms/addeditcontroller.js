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
            $location.path('/forms/' + id + '/entries');
        }).finally(function() {
            $scope.saving = false;
        });
      } else {
        $scope.damnForm.$save().then(function () {
            $location.path('/forms/' + id + '/entries');
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

    $scope.parseForm = function (html) {
      var schema = [];

      //Parse Input Tags
      var isMandatory = false;
      var inputTags = html.match(/<input.*\/>/g);
      if (inputTags) {
        for(var index in inputTags) {
          var inputTag = inputTags[index],
            type = inputTag.match(/type=\"(.*?)\"/)[1],
            name = inputTag.match(/name=\"(.*?)\"/)[1],
            mandatoryMatch = inputTag.match(/required/);

            if (type && name) {
              var fieldType = type;
              if (fieldType === 'text') {
                fieldType = 'string';
              } else if (fieldType === 'checkbox') {
                fieldType = 'boolean';
              }
              schema.push({name: name, type: fieldType, mandatory: mandatoryMatch ? true : false});
            }
        }
      }

      //Parse TextAreas and Select Tag
      var textareaTags = html.match(/<textarea .*>.*<\/textarea>|<select .*>/g);
      if (textareaTags) {
        for(var index in textareaTags) {
          var textareaTag = textareaTags[index],
            name = textareaTag.match(/name=\"(.*?)\"/)[1],
            mandatoryMatch = textareaTag.match(/required/);
            if (name) {
              schema.push({name:name, type: string, mandatory: mandatoryMatch ? true : false});
            }

        }
      }

      console.log(schema);
      if (schema.length > 0) {
        $scope.damnForm.schema = schema;
      }
      return schema;
    }
});
