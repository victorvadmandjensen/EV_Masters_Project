// all noble attempts that currently only work in the .html pages

document.getElementById("start_season").onclick = function () {
    location.href = "/event";
};

document.getElementById("end_round").onclick = function () {
    location.href = "/energy_decision";
};

document.getElementById("next_event").onclick = function () {
    location.href = "/event";
};

document.getElementById("start_thm").onclick = function () {
    location.href = "/town_hall_meeting";
};

document.getElementById("start_vote").onclick = function () {
    location.href = "/upgrades";
};