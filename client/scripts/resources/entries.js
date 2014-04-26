//
// Entries Resource
//

angular.module('myApp').factory('Entries', function ($resource) {

    var entriesResource =  $resource('/api/forms/:formId/entries/:id', { id: '@_id.$oid' });

    return entriesResource;
});
