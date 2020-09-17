function sethearts(value) {
    var el1 = document.getElementById('hearts');
    var el2 = document.getElementById('health');
    var hearts = Number(el1.textContent);
    var health = Number(el2.textContent);
    
    if ((hearts + (value*-1) >= 0) && (hearts + (value*-1) <= 10)) {
        el1.innerHTML = hearts + (value*-1);
        el2.innerHTML = health + value;
    }
    else {
        // 처리코드
    }
}
var elr = document.getElementById('right');
var ell = document.getElementById('left');
elr.onclick = function() {sethearts(1);};
ell.onclick = function() {sethearts(-1);};