//
// Mails Resource
//

angular.module('myApp').factory('Mails', function ($resource) {

    var mailsResource =  $resource('/api/forms/:form_id/sendmail',
                              { form_id: '@form_id.$oid' },
                              { update: { method: 'PUT' } });

    return mailsResource;
});
