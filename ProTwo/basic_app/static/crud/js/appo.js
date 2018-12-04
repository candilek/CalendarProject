

    $(document).on('click', '.delete', function(){
      $id = $(this).attr('name');
      $.ajax({
          url: 'appo_delete/' + $id,
          type: 'POST',
          data: {
              csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
          },
          success: function(){
              Read();
              alert("Deleted!");
          }
      });
  });

});
