    var board_name = ""
    var board_id  = 0
    function topicsTable (){
      $('#topics-table') .bootstrapTable({                        
        url: "/boards/api/topic/query_board_topic/",
        data:{'board':board_name},       
        dataType:"json",
        classes:'table',
        method:'get',     
        pagination : true, 
        pageSize : 15,    
        height:500,
        buttons :"buttons",
        toolbar :"#toolbar",
        uniqueId :"id",
        filterBy:{
          board:board_name,
        },
        columns: [ 
              { 
                field :"subject",
                title:'Topic',
                formatter:nameFormatter,                             
              },
              { 
                field :"starter.username", 
                title:'Starter',                                                    
              },      
              { 
                field :"get_post_count", 
                title:'Replies',                                                    
              },      
              { 
                field :"views", 
                title:'Views',                                                    
              },  
              { 
                field :"get_last_post", 
                title:'Last Update',                                                    
              },                      
          ],

        }); 

    function nameFormatter(value, row, index){
          var html = []
          html.push('<a href="#">' + value + "</a>")      
          return html.join('')
        } 
    }
    $("#add").click(function (e) { 
      e.preventDefault();
      $('#topic-modal-create').modal()                       
    }); 


    function saveTopic(){
      var form = $(this);   
      
      //var data = form.serialize() + "&board=1"
      var data = form.serializeArray();  
      data.push({name: "board", value: board_id})
      data = jQuery.param(data)

      $.ajax({
        headers: {
              'X-CSRFTOKEN': '{{ csrf_token }}'
        },
        dataType: 'json',
        method: form.attr('method'),
        url: form.attr('data-url'),        
        //data: form.serialize(), 
        data: data,
        success: function (response) {
          location.reload();
            console.log("success")
        },
        error: function (jqXHR, textStatus, errorThrown) {                      
          console.log(jqXHR)
        }, 
      });
    } 
    
    function initial(bname,id){
         board_name = bname;
         board_id = id
         topicsTable()
    }    
    //$('form').on('submit',saveTopic)
    $("#topic-modal-create").on("submit", ".js-create-topic", saveTopic);
    

    
    
    
    
    
    
    
    
    
    
    
    