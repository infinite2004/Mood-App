var text  = [ "continue to be happy", "always smile", "nice smile", "continue being awsome", "" ];
var index = 0;
$("#description").fadeTo( 1, 0 );
setInterval( function(){
    $( "#description" ).stop().html( text[ index ] ).fadeTo( 500, 1, function(){
        index++;
        $( "#description" ).delay( 600 ).fadeTo( 500, 0 );
        if ( index == 10 ) {
            index = 0;
        };
    } );
}, 1800 );

var SAD  = [ "better days will come", "dont give up", "keep your head up", "continue being awsome", "look to the future" ];
var index = 0;
$("#SAD").fadeTo( 1, 0 );
setInterval( function(){
    $( "#SAD" ).stop().html( SAD[ index ] ).fadeTo( 500, 1, function(){
        index++;
        $( "#SAD" ).delay( 600 ).fadeTo( 500, 0 );
        if ( index == 10 ) {
            index = 0;
        };
    } );
}, 1800 );