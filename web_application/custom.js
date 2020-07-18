$( document ).ready(function() {

    console.log( "ready!" );

    $('form').submit(function(event){

      event.preventDefault();
      var formData = new FormData();
      formData.append("name", $('#title').val());
      formData.append("CCTV_Main_Img", $('#filename')[0].files[0]);
      console.log(formData);

      var action_error = function(d){
        console.log(d);
      }

      var changeImg = function(d){
        var new_location = 'http://127.0.0.1:8000/' + d["new_path"];
        var old_location = d["original_path"]
        $("#outputImage").attr("src",new_location);
        $("#inputImage").attr("src",old_location);
        //console.log(old_location)
      };

      //var printResponse = function()

      $.ajax({
        url: 'http://127.0.0.1:8000/upload/',
        data: formData,
        dataType: 'json',
        cache: false,
        contentType: false,
        processData: false,
        type: 'POST',
        success: changeImg,
        error: action_error
      });
    });
});
