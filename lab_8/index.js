
$(function () {
    var from = $('#from');
    var to = $('#to');
    var func = $('#func');
    var out = $('#output');

    $('#plot').click(function (event) {
        event.preventDefault();
        var array = [];
        var start = parseFloat(from.val());
        var end = parseFloat(to.val());
        for (var x = start; x < end; x += (end - start) / 100) {
            array.push([x, eval(func.val())]);
        }
        console.log(array);
        $.plot(out, [array]);
    })
})