//
// Entries Resource
//

angular.module('myApp').factory('Entries', function ($resource) {

    var entriesResource =  $resource('/api/forms/:form_id/entries/:id',
                              { id: '@_id.$oid', form_id: '@form_id.$oid' },
                              { update: { method: 'PUT' } });

    return entriesResource;
});
