/*-----------------------------------------------------------------------------
 * String.format
 *-------------------------------------------------------------------------- */

String.prototype.format = function() {
    var txt = this, i = arguments.length; while (i--) {
        txt = txt.replace (
            new RegExp('\\{' + i + '\\}', 'gm'), arguments[i]
        );
    }

    return txt;
};
