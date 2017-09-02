(function() {
    jQuery(document).ready(function() {
        jQuery('[data-toggle="tooltip"]').tooltip();
    });
})();

(function() {
    jQuery(document).ready(function() {
        jQuery('.rgm-confirm-link').each(function() {
            var linkQ = jQuery(this);
            linkQ.click(function(event) {
                var message = linkQ.data('rgmconfirmessage');
                if (typeof message != 'undefined' && message != null && !confirm(message)) {
                    event.preventDefault();
                    return false;
                }
            });
        });
    });
})();