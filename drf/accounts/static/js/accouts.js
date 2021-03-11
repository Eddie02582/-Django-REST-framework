    function initialUserTable (){
      $('#user-table') .bootstrapTable({                        
          url: "/accounts/api/user/",
        showColumns : true,
        showColumnsToggleAll:true, //在欄位選擇開啟開關全部欄位
        showToggle : true, //名片式/table式切換
        showPaginationSwitch : true, //分頁/不分頁切換
        showRefresh : true, //重新整理
        showFullscreen: true,
        search : true, //查詢 
        pagination : true, 
        pageSize : 15,    
        height:500,
        buttons :"buttons",
        toolbar :"#toolbar",
        uniqueId :"id",
        columns: [ 
              {               
                title:'State',
                checkbox:true,                               
              },
              { 
                field :"id",
                title:'ID',
                visible:false, 
              },
              { 
                field :"username",
                title:'User Name',                             
              },
              { 
                field :"first_name", 
                title:'First Name',                                                    
              },      
              { 
                field :"last_name", 
                title:'Last Name',                                                    
              },      
              { 
                field :"email", 
                title:'Email',                                                    
              },   
              { 
                field :"profile.cell_phone_number", 
                title:'Cell Phone',                                                    
              }, 
              { 
                field :"profile.points", 
                title:'Points',                                                    
              },                 
          ],
        })   
    }

    function getIdSelections() {
      return $.map($('#user-table').bootstrapTable('getSelections'), function (row) {
          return row.id
      })
    }


    $('#user-table').on('check.bs.table uncheck.bs.table ',function () {
        $("#edit").prop('disabled', !$('#user-table').bootstrapTable('getSelections').length)                     
                              
    })

    $("#edit").click(function (e) { 
        e.preventDefault();
        $('#user-update-modal').modal()                   
        var id = getIdSelections();                     
        var data = $('#user-table').bootstrapTable('getRowByUniqueId', id)
        $('#username').val(data.username)
        $('#first_name').val(data.first_name)
        $('#last_name').val(data.last_name)
        $('#email').val(data.email)                  
        $('#cell_phone_number').val(data['profile'].cell_phone_number)
        $('#points').val(data['profile'].points)
        $('form').attr('data-url',"/accounts/api/user/" + id +"/")
    });

    $("#add").click(function (e) { 
        e.preventDefault();
        $('#user-modal-create').modal()                       
    }); 

    function saveUser(){
      var form = $(this);             
      $.ajax({
        headers: {
            'X-CSRFTOKEN': '{{ csrf_token }}'
        },
      
        dataType: 'json',
        method: form.attr('method'),
        url: form.attr('data-url'),
        data: form.serialize(), 
        //data: formData  ,   
        //cache:false,
        //processData : false,
        //contentType: false,             
        success: function (response) {
          location.reload();
            console.log("success")
        },
        error: function (jqXHR, textStatus, errorThrown) {                      
          console.log(jqXHR)
        },   
      });                  
      return false;
    }
    $('form').on('submit',saveUser)
