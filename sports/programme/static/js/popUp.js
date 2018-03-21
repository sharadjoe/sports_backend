function popUp(message, pk){

    if (confirm(''+message +pk)) {
        window.location.href = "/programmes/delete/" +pk;
    }                                
}