var subjectObject = {
    "ABC": ['A', 'B', 'C'],
    "DEF": ['D', 'E'],
}
window.onload = function () {
    var subjectSel = document.getElementById("subject");
    var chapterSel = document.getElementById("chapter");
    for (var x in subjectObject) {
        subjectSel.options[subjectSel.options.length] = new Option(x, x);
    }
    subjectSel.onchange = function () {
        chapterSel.length = 1;
        for (var y of subjectObject[this.value]) {
            chapterSel.options[chapterSel.options.length] = new Option(y, y);
        }
    }
}

