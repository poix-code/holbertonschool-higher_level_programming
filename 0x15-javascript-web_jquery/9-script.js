$(document).ready(function () {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
    $('#hello').html(data.hello);
  });
});
