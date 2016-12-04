// /**
//  * Created by Filip on 06.11.2016.
//  */
//
//
// $(document).ready(function () {
//     loadDaysOfTheWeek()
// });
//
// var loadWeekSchedule = function () {
//     $.ajax({
//         url: "http://localhost:8000/classes",
//         type: "GET",
//         dataType: "json"
//     }).done(function (json) {
//         alert(json.results[0].name);
//     }).fail(function (xhr, status, errorThrown) {
//         alert("Error" + "**" + xhr + "**" + status + "**" + errorThrown);
//     })
// }
//
// var loadDaysOfTheWeek = function () {
//     $.ajax({
//         url: "http://localhost:8000/week/days",
//         type: "GET",
//         dataType: "json"
//     }).done(function (days) {
//         fillScheduleDayNames(JSON.parse(days))
//     }).fail(function (xhr, status, errorThrown) {
//         alert("Error" + "**" + xhr + "**" + status + "**" + errorThrown);
//     })
// };
//
// var fillScheduleDayNames = function (days) {
//     $(".day").each(function(index, object){
//         $(this).text(days[index])
//     })
// }