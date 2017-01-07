/**
 * Created by Filip on 07.01.2017.
 */

gymApp.filter("nl2br", function($filter) {
 return function(data) {
   if (!data) return data;
   return data.replace(/\n\r?/g, '<br />');
 };
});