//
// Form Resource
//

angular.module('myApp').factory('Forms', function ($resource) {

    var formResource =  $resource('/api/forms/:id', { id: '@_id.$oid' });

    return formResource;
});
