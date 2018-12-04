

    $(document).on('click', '.delete', function(){
      $id = $(this).attr('name');
      var yanit = confirm("Are you sure you want to delete?");
	     if(yanit == true) {
      $.ajax({
          url: 'visitor_delete/' + $id,
          type: 'POST',
          data: {
              csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
          },
          success: function(){
              alert('Deleted!');
            $(id).fadeOut();
            window.location = '/';
            alert('Deleted!');
          }
      });
  });
});

});
